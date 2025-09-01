from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tool, FarToolCategory
from .serializer import ToolSerializer, FarToolCategorySerializer
from rest_framework import generics


class FarToolCategoryView(APIView):
    def get(self, request):
        # 如果是API请求，返回JSON数据
        if request.headers.get('Content-Type') == 'application/json' or request.headers.get('Accept') == 'application/json':
            f = FarToolCategory.objects.all()
            ser = FarToolCategorySerializer(f, many=True)
            return Response(ser.data, status=200)
        # 否则渲染HTML模板
        else:
            categories = FarToolCategory.objects.all()
            tools = Tool.objects.all()
            return render(request, 'tool_categories.html', {
                'categories': categories,
                'tools': tools
            })

    def post(self, request):
        # 如果是API请求，返回JSON数据
        if request.headers.get('Content-Type') == 'application/json':
            ser = FarToolCategorySerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=201)
            else:
                return Response(ser.errors, status=400)
        # 否则处理表单提交并重定向
        else:
            ser = FarToolCategorySerializer(data=request.POST)
            if ser.is_valid():
                ser.save()
                return redirect('/tools/categories/')
            else:
                categories = FarToolCategory.objects.all()
                tools = Tool.objects.all()
                return render(request, 'tool_categories.html', {
                    'categories': categories,
                    'tools': tools,
                    'errors': ser.errors
                })


class FarToolCategoryNumView(APIView):
    def get(self, request, pk):
        # 如果是API请求，返回JSON数据
        if request.headers.get('Content-Type') == 'application/json' or request.headers.get('Accept') == 'application/json':
            try:
                f = FarToolCategory.objects.get(pk=pk)
                ser = FarToolCategorySerializer(f)
                return Response(ser.data, status=200)
            except FarToolCategory.DoesNotExist:
                return Response({'error': '分类不存在'}, status=404)
        # 否则重定向到分类列表页面
        else:
            return redirect('/tools/categories/')

    def put(self, request, pk):
        """修改"""
        # 如果是API请求，返回JSON数据
        if request.headers.get('Content-Type') == 'application/json':
            try:
                f = FarToolCategory.objects.get(pk=pk)
                ser = FarToolCategorySerializer(f, data=request.data)
                if ser.is_valid():
                    ser.save()
                    return Response(ser.data, status=200)
                else:
                    return Response(ser.errors, status=400)
            except FarToolCategory.DoesNotExist:
                return Response({'error': '分类不存在'}, status=404)
        # 否则处理表单提交并重定向
        else:
            try:
                f = FarToolCategory.objects.get(pk=pk)
                ser = FarToolCategorySerializer(f, data=request.POST)
                if ser.is_valid():
                    ser.save()
                    return redirect('/tools/categories/')
                else:
                    categories = FarToolCategory.objects.all()
                    tools = Tool.objects.all()
                    return render(request, 'tool_categories.html', {
                        'categories': categories,
                        'tools': tools,
                        'errors': ser.errors
                    })
            except FarToolCategory.DoesNotExist:
                return redirect('/tools/categories/')

    def delete(self, request, pk):
        # 如果是API请求，返回JSON数据
        if request.headers.get('Content-Type') == 'application/json':
            try:
                f = FarToolCategory.objects.get(pk=pk)
                f.delete()
                return Response({'msg': '删除成功'}, status=204)
            except FarToolCategory.DoesNotExist:
                return Response({'error': '分类不存在'}, status=404)
        # 否则重定向到分类列表页面
        else:
            try:
                f = FarToolCategory.objects.get(pk=pk)
                f.delete()
                return redirect('/tools/categories/')
            except FarToolCategory.DoesNotExist:
                return redirect('/tools/categories/')




class ToolListCreateView(generics.ListCreateAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    
    def get(self, request, *args, **kwargs):
        # 如果是API请求，返回JSON数据
        if request.headers.get('Content-Type') == 'application/json' or request.headers.get('Accept') == 'application/json':
            return super().get(request, *args, **kwargs)
        # 否则渲染HTML模板
        else:
            tools = self.get_queryset()
            categories = FarToolCategory.objects.all()
            return render(request, 'tools.html', {
                'tools': tools,
                'categories': categories
            })
    
    def post(self, request, *args, **kwargs):
        # 如果是API请求，返回JSON数据
        if request.headers.get('Content-Type') == 'application/json':
            return super().post(request, *args, **kwargs)
        # 否则处理表单提交并重定向
        else:
            serializer = self.get_serializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return redirect('/tools/')
            else:
                tools = self.get_queryset()
                categories = FarToolCategory.objects.all()
                return render(request, 'tools.html', {
                    'tools': tools,
                    'categories': categories,
                    'errors': serializer.errors
                })


class ToolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    
    def get(self, request, *args, **kwargs):
        # 如果是API请求，返回JSON数据
        if request.headers.get('Content-Type') == 'application/json' or request.headers.get('Accept') == 'application/json':
            return super().get(request, *args, **kwargs)
        # 否则重定向到工具列表页面
        else:
            return redirect('/tools/')
