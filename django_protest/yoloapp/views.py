import os
from django.shortcuts import render
from rest_framework.views import APIView
from ultralytics import YOLO
from django_protest import settings
from .models import YoLoModel


class YololistView(APIView):
    def get(self,request):
        return render(request, 'yolo.html')

    def post(self, request):
        u = YoLoModel()
        u.img = request.FILES.get('img')

        if u.img:
            # 1. 保存上传的原始图片
            u.save()

            # 2. YOLO 预测
            model = YOLO(model=r'F:\jdango_pro\django_protest\yoloapp\weight\last.pt')
            # model.predict(
            #     source=u.img.path,
            #     save=True,  # 保存结果到 runs/detect/exp/
            #     show=False,  # 服务器不要 show
            # )
            model.predict(
                source=u.img.path,
                save=True,
                project='runs/detect',
                name='predict',
                exist_ok=True,
                show=False,
            )
            print("预测成功")

            result_image_name = os.path.basename(u.img.path)
            result_src_path = os.path.join(settings.BASE_DIR,'runs', 'detect', 'predict', result_image_name)

            if not os.path.exists(result_src_path):
                return render(request, "yoloshow.html", {
                    'u': u,
                    'error': '预测结果图未生成，请检查 runs/detect/exp/'
                })
            predicted_image_url = f"{settings.RUNS_URL}detect/predict/{result_image_name}"
            print(f"Predicted image URL: {predicted_image_url}")

            return render(request, "yoloshow.html", {
                'predicted_image_url': predicted_image_url
            })
        else:
            return render(request, "upload_file.html", {
                'error': '请上传图片'
            })