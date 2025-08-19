from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response


class StudentList(APIView):
    def get(self,request,format=None):
        stus = Student.objects.all()
        ser = StudentSerializer(stus,many=True)
        return Response(ser.data)

    def post(self,request,format=None):
        """
        增加直接传json
        :param request:
        :param format:
        :return:
        """
        ser = StudentSerializer(request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors,status=400)


class StudentDetail(APIView):

    def get(self,request,pk,format=None):
        try:
            stu = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return JsonResponse({'error': '学生不存在'}, status=404)
        ser = StudentSerializer(stu)
        return Response(ser.data,status=200)
    def put(self, request, pk, format=None):
        try:
            stu = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return JsonResponse({'error': '学生不存在'}, status=404)
        ser = StudentSerializer(stu,data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=201)
    def delete(self, request, pk, format=None):
        try:
            stu = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return JsonResponse({'error': '学生不存在'}, status=404)

        stu.delete()
        return Response({'msg': '删除成功'}, status=204)