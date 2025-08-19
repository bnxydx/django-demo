from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


class StudentList(GenericAPIView):
    # 指定查询集
    queryset = Student.objects.all()
    # 指定序列化
    serializer_class = StudentSerializer

    def get(self, request, format=None):
        # 获取数据集
        stus = self.get_queryset()
        #序列化
        ser = self.get_serializer(stus, many=True)
        return Response(ser.data)

    def post(self, request, format=None):
        """
        增加直接传json
        """
        ser = self.get_serializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors, status=400)


class StudentDetail(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk, format=None):
        try:
            stu = self.get_object()
        except Student.DoesNotExist:
            return JsonResponse({'error': '学生不存在'}, status=404)
        ser = self.get_serializer(stu)
        return Response(ser.data, status=200)

    def put(self, request, pk, format=None):
        try:
            stu = self.get_object()
        except Student.DoesNotExist:
            return JsonResponse({'error': '学生不存在'}, status=404)
        ser = self.get_serializer(stu, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)

    def delete(self, request, pk, format=None):
        try:
            stu = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return JsonResponse({'error': '学生不存在'}, status=404)

        stu.delete()
        return Response({'msg': '删除成功'}, status=204)
