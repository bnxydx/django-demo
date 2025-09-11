from rest_framework.serializers import ModelSerializer
from .models import YoloModels

class YoloSerializers(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = YoloModels