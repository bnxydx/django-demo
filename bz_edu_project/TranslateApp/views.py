from django.shortcuts import render
from rest_framework.views import APIView
from .utils.Translate_tool import translate
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class TranslateView(APIView):
    def post(self,request):
        text = request.data.get('text')
        if not text:
            return Response(status=400, data={
                'error': '请提供要翻译的文本'
            })
        text_translated = translate(text)
        return Response(status=200, data={
            'original': text,
            'translated': text_translated
        })
    
    def get(self, request):
        # 用于前端页面展示
        return Response(status=200, data={
            'message': '翻译服务正常运行'
        })
