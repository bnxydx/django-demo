from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
# Create your views here.

def request_index(request):
    print(type(request))
    print(request.path)
    print(request.method)
    print(request.scheme)
    return HttpResponse('测试')

def upload_image(request):
    if request.method == 'POST':
        # 获取上传的图片
        image = request.FILES.get('image')
        if image:
            # 创建保存路径
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
            # 确保目录存在
            os.makedirs(upload_dir, exist_ok=True)
            # 构建完整的文件路径
            file_path = os.path.join(upload_dir, image.name)
            
            # 保存图片到本地
            with open(file_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            
            # 构建图片URL
            image_url = f"{settings.MEDIA_URL}uploads/{image.name}"
            
            # 打印图片信息
            print(f"接收到图片: {image.name}")
            print(f"保存路径: {file_path}")
            
            # 返回成功信息和图片URL
            return HttpResponse(f'图片上传成功！<br>图片名称: {image.name}<br><a href="{image_url}" target="_blank">查看图片</a>')
        else:
            return HttpResponse('未接收到图片文件', status=400)
    else:
        # 如果是GET请求，返回上传页面
        return render(request, 'upload/upload_form.html')