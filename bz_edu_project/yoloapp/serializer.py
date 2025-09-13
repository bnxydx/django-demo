from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import YoloModels
import os
from django.conf import settings


class YoloSerializers(ModelSerializer):
    img = SerializerMethodField()
    original_image_url = SerializerMethodField()
    predicted_image_url = SerializerMethodField()

    class Meta:
        fields = ['id', 'img', 'original_image_url', 'predicted_image_url']
        model = YoloModels

    def get_img(self, obj):
        """返回原始上传图片的URL"""
        if obj.img:
            return obj.img.url
        return None

    def get_original_image_url(self, obj):
        """返回原始上传图片的URL"""
        if obj.img:
            return obj.img.url
        return None

    def get_predicted_image_url(self, obj):
        """返回预测结果图片的URL"""
        if obj.img:
            # 根据原始图名推测预测图路径
            img_name = os.path.basename(obj.img.name)  # 如 "test.jpg"
            predicted_path = f"{settings.RUNS_URL}detect/predict/{img_name}"
            
            # 检查预测图是否存在
            full_predicted_path = os.path.join(settings.RUNS_ROOT, 'detect', 'predict', img_name)
            if os.path.exists(full_predicted_path):
                return predicted_path
            else:
                # 如果预测图不存在，返回原图
                return obj.img.url
        return None
