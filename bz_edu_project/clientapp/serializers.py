from rest_framework import serializers
from .models import ClientModel


class ClientSerializers(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()
    
    class Meta:
        model = ClientModel
        fields = '__all__'
    
    def get_time(self, obj):
        if obj.time:
            # 直接返回数据库中的时间，不进行任何时区转换
            # 假设数据库中存储的就是本地时间
            return obj.time.strftime('%Y-%m-%d %H:%M:%S')
        return None

# class ClientHistorySerializers(Serializer):
#
#     class Meta:
#         models = ClientModel
#         fields = ['co2','']
