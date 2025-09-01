from django.shortcuts import render
from .models import Student, Classes
from .serializers import StudentSerializer, ClassSerializer,Class2Serializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

'''
对学生执行 增删改查API：
   行为       请求方式   请求路径URL
   增加       POST     /students/
   删除       DELETE    /student/<int:id>/
   修改       PUT     /student/<int:id>/
   查询一个     GET     /student/<int:id>/
   查询所有     GET     /students/
'''


def index(request):
    stu = Student.objects.all()
    ser = StudentSerializer(stu, many=True)
    return JsonResponse(ser.data, safe=False)


def classes_detail(request, pk):
    try:
        classes = Classes.objects.get(pk=pk)
    except Classes.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Class2Serializer(classes)
        return JsonResponse(serializer.data)
    else:
        # 其他情况暂不处理
        return HttpResponse(status=503)


@csrf_exempt
# Create your views here.
def students(request):
    if request.method == 'GET':
        # 查询所有
        stus = Student.objects.all()
        serializer = StudentSerializer(stus, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser = StudentSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        else:
            return JsonResponse(ser.errors, status=400)


@csrf_exempt
def student(request, id):
    try:
        stu = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return JsonResponse({'error': '学生不存在'}, status=404)

    if request.method == 'GET':
        ser = StudentSerializer(stu)
        return JsonResponse(ser.data)
    elif request.method == 'PUT':
        # 修改
        data = JSONParser().parse(request)
        ser = StudentSerializer(stu, data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=200)
        else:
            return JsonResponse(ser.errors, status=400)
    elif request.method == 'DELETE':
        stu.delete()
        return HttpResponse(status=204)
