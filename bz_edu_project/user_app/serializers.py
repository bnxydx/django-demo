from rest_framework import serializers
from .models import User


# 创建注册序列化器
class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=11, min_length=3, required=True)
    password = serializers.CharField(max_length=32, min_length=3, required=True)
    nickname = serializers.CharField(required=False)
    gender = serializers.IntegerField(required=False)
    job_title = serializers.CharField(required=False)
    introduction = serializers.CharField(required=False)
    avatar = serializers.CharField(required=False)

    # 验证手机号是否已经注册
    def validate_phone(self, value):
        try:
            User.objects.get(phone=value)
            raise serializers.ValidationError('手机号已经注册')
        except User.DoesNotExist:
            return value

    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # 不序列化的字段
        exclude = ('create_at', 'update_at', '_password')
