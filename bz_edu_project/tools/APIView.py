from .models import Tool, FarToolCategory
from .serializer import ToolSerializer, FarToolCategorySerializer
from rest_framework import generics


class FarToolCategoryView(generics.ListCreateAPIView):
    queryset = FarToolCategory.objects.all()
    serializer_class = FarToolCategorySerializer


class FarToolCategoryNumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FarToolCategory.objects.all()
    serializer_class = FarToolCategorySerializer


class ToolListCreateView(generics.ListCreateAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer


class ToolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
