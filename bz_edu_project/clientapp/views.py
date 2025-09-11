from rest_framework.generics import ListAPIView,CreateAPIView
from django.utils import timezone
from datetime import datetime
from .models import ClientModel
from .serializers import ClientSerializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.shortcuts import render
import pytz

# Create your views here.

def data_visualization_view(request):
    """数据可视化页面"""
    return render(request, 'data_visualization.html')

def data_upload_view(request):
    """数据上传页面"""
    return render(request, 'data_upload.html')

class ClientListView(ListAPIView):
    serializer_class = ClientSerializers

    def get_queryset(self):
        # 获取 URL 参数
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        queryset = ClientModel.objects.all()

        if start:
            try:
                start_dt = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
                # 简单处理：假设传入的时间就是本地时间，直接使用
                queryset = queryset.filter(time__gte=start_dt)
            except ValueError:
                pass

        if end:
            try:
                end_dt = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
                # 简单处理：假设传入的时间就是本地时间，直接使用
                queryset = queryset.filter(time__lte=end_dt)
            except ValueError:
                pass

        return queryset


class ClientAddView(CreateAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializers
