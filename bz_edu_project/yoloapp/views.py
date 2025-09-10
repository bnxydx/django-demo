import os
from pathlib import Path
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from bz_edu_project import settings
from .models import YoloModels
from ultralytics import YOLO
from .utils.SendEmail import send_email
class YoloListView(APIView):
    def get(self,request):
        return render(request,'yolo.html')

    def post(self,request):
        u = YoloModels()
        u.img = request.FILES.get('img')

        if u.img:
            u.save()
            weight_path = Path(__file__).parent / "weight" / "last.pt"
            model = YOLO(model=weight_path)
            model.model.names = ['dead']
            model.predict(
                source=u.img.path,
                save=True,
                project='runs/detect',
                name='predict',
                exist_ok=True,
                show=False,
                save_conf=True,
                save_txt=True,
            )

            result_image_name = os.path.basename(u.img.path)
            result_src_path = os.path.join(settings.BASE_DIR, 'runs', 'detect', 'predict', result_image_name)

            if not os.path.exists(result_src_path):
                return render(request, "yoloshow.html", {
                    'u': u,
                    'error': '预测结果图未生成，请检查 runs/detect/exp/'
                })
            predicted_image_url = f"{settings.RUNS_URL}detect/predict/{result_image_name}"
            img_txt = f"{settings.RUNS_URL}detect/predict/labels/{result_image_name}"
            img_txt = '.' + img_txt[:-3] + 'txt'
            print(img_txt)
            num = 0
            with open(img_txt,'r') as f:
                s = f.readline()
                l = s.split()
                num = l[-1]
            # print(f"Predicted image URL: {predicted_image_url}")

            return render(request, "yoloshow.html", {
                'predicted_image_url': predicted_image_url,
                'score': num
            })
        else:
            return render(request, "yolo.html", {
                'error': '请上传图片'
            })


class SendEmailView(APIView):
    def post(self, request):
        """接收前端传入的分数并调用工具函数发送邮件"""
        score = request.data.get('score') or request.POST.get('score')
        Qnum = request.data.get('Qnum')
        if not score:
            return Response({"message": "缺少分数参数"}, status=400)
        try:
            send_email(score,Qnum)
            return Response({"message": "邮件已发送"}, status=200)
        except Exception as exc:
            return Response({"message": f"发送失败: {exc}"}, status=500)