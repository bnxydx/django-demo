from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Tool, FarToolCategory


class ToolSerializer(ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Tool
        fields = ['id', 'name', 'description', 'url', 'category', 'category_name']


class FarToolCategorySerializer(ModelSerializer):
    tools = ToolSerializer(many=True, read_only=True)  # 注意：related_name='tools'

    class Meta:
        model = FarToolCategory
        fields = ['id', 'name', 'tools']
