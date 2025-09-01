from rest_framework import serializers
from .models import Student, Classes


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    classes = ClassSerializer()

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'sex', 'classes']


class Class2Serializer(serializers.ModelSerializer):
    # 通过related_name反向查询的字段，创建序列化器对象
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Classes
        fields = ['id', 'name', 'students']
