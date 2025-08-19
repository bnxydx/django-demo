from rest_framework.serializers import ModelSerializer
from .models import Tools

class ToolSerializers(ModelSerializer):
    class Meta:
        model = Tools
        fields = '__all__'