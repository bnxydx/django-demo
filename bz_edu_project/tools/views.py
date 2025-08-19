from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.
from rest_framework.response import Response
from .models import Tools
from .serializer import ToolSerializers
class ToolsView(generics.GenericAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolSerializers
    def get(self,request):
        d = self.get_queryset()
        # 如果是API请求，返回JSON数据
        if request.headers.get('Content-Type') == 'application/json' or request.headers.get('Accept') == 'application/json':
            ser = self.get_serializer(d,many=True)
            return Response(ser.data)
        # 否则渲染HTML模板
        else:
            return render(request, 'tools.html', {'tools': d})

    def post(self,request):
        ser = self.get_serializer(data = request.data)
        if ser.is_valid():
            ser.save()
            # 如果是API请求，返回JSON数据
            if request.headers.get('Content-Type') == 'application/json':
                return Response(ser.data, status=201)
            # 否则重定向到GET页面
            else:
                return redirect('/tools/')
        
        # 如果是API请求，返回错误JSON
        if request.headers.get('Content-Type') == 'application/json':
            return Response(ser.errors, status=400)
        # 否则重新渲染页面并显示错误
        else:
            d = self.get_queryset()
            return render(request, 'tools.html', {'tools': d, 'errors': ser.errors})


    def put(self, request, pk):
        try:
            tool = Tools.objects.get(pk=pk)
        except Tools.DoesNotExist:
            return Response({'error': '工具不存在'}, status=404)
        
        ser = self.get_serializer(tool, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=200)
        else:
            return Response(ser.errors, status=400)

    def delete(self,request,pk):
        try:
            t = Tools.objects.get(pk=pk)
        except Tools.DoesNotExist:
            return Response({'error': '工具不存在'}, status=404)
        
        t.delete()
        return Response({'msg': '删除成功'}, status=204)