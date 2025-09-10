from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tool, FarToolCategory
from .serializer import ToolSerializer, FarToolCategorySerializer
from rest_framework import generics

class FarToolCategoryView(generics.ListCreateAPIView):
    queryset = FarToolCategory.objects.all()
    serializer_class = FarToolCategorySerializer

# class FarToolCategoryView(APIView):
    # def get(self, request):
    #     f = FarToolCategory.objects.all()
    #     ser = FarToolCategorySerializer(f, many=True)
    #     return Response(ser.data, status=200)
    #
    # def post(self, request):
    #     ser = FarToolCategorySerializer(data=request.data)
    #     if ser.is_valid():
    #         ser.save()
    #         return Response(ser.data, status=201)
    #     else:
    #         return Response(ser.errors, status=400)


class FarToolCategoryNumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FarToolCategory.objects.all()
    serializer_class = FarToolCategorySerializer
# class FarToolCategoryNumView(APIView):
#     def get(self, request, pk):
#         f = FarToolCategory.objects.get(pk=pk)
#         ser = FarToolCategorySerializer(f)
#         return Response(ser.data, status=200)
#
#     def put(self, request, pk):
#         """修改"""
#         f = FarToolCategory.objects.get(pk=pk)
#         ser = FarToolCategorySerializer(f, data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=201)
#         else:
#             return Response(ser.errors, status=400)
#
#     def delete(self, request, pk):
#         f = FarToolCategory.objects.get(pk=pk)
#         f.delete()
#         return Response({'msg': '删除成功'}, status=204)


class ToolListCreateView(generics.ListCreateAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer


class ToolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
