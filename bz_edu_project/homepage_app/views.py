from django.shortcuts import render
from .models import RotationChart
from .serilizers import RotationChartListSerilizers
# Create your views here.
from rest_framework import generics


class RotationChartView(generics.ListAPIView):
    queryset = RotationChart.objects.all().order_by('-id')
    serializer_class = RotationChartListSerilizers
