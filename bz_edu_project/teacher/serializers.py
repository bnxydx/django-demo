from rest_framework.serializers import ModelSerializer

from .models import Teacher

class TeacherListSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'