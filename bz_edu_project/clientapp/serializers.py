from rest_framework import serializers
from .models import ClientModel


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'

# class ClientHistorySerializers(Serializer):
#
#     class Meta:
#         models = ClientModel
#         fields = ['co2','']
