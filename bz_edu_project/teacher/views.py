from rest_framework import generics
from .models import Teacher
from .serializers import TeacherListSerializer


class TeacherListViews(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
