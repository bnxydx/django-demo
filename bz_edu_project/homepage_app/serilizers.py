from rest_framework.serializers import Serializer
from .models import RotationChart

class RotationChartListSerilizers(Serializer):
    class Meta:
        model = RotationChart
        fields = '__all__'