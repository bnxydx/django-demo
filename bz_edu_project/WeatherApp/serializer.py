from rest_framework.serializers import ModelSerializer
from .models import WeatherModels
class WeatherSerializers(ModelSerializer):
    class Meta:
        model = WeatherModels
        fields = ['Qnum','City']