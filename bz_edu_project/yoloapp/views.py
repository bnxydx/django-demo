import os

from django.shortcuts import render
from rest_framework.views import APIView

from bz_edu_project import settings
from .models import YoloModels
# Create your views here.
from ultralytics import YOLO

class YoloListView(APIView):
    def get(self,request):
        return render(request,'yolo.html')

    def post(self,request):
        u = YoloModels()
        u.img = request.FILES.get('img')

        if u.img:
            u.save()
            model = YOLO(model=r'F:\jdango_pro\bz_edu_project\yoloapp\weight\last.pt')
            model.predict(
                source=u.img.path,
                save=True,
                project='runs/detect',
                name='predict',
                exist_ok=True,
                show=False,
            )
            result_image_name = os.path.basename(u.img.path)
            result_src_path = os.path.join(settings.BASE_DIR, 'runs', 'detect', 'predict', result_image_name)

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
            return render(request, "yolo.html", {
                'error': '请上传图片'
            })