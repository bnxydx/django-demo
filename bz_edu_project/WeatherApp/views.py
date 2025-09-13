from django.shortcuts import render
from .utils.weather_q import weather_query
from .utils.SendWeatherData import send_email
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework.generics import ListAPIView
from .serializer import WeatherSerializers
from .models import WeatherModels
from .tasks import se
class WeatherView(APIView):
    def get(self,request):
        return render(request,'weather.html')

    def post(self,request):
        city = request.data.get('text')
        data = weather_query(city)
        return Response(status=200,data=data)


class SubscribeWeatherView(APIView):
    def get(self,request):
        return render(request,'Weather_sub.html')
    def post(self,request):
        ser = WeatherSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        else:
            return Response(ser.errors, status=400)


class SendWeatherData(APIView):

    def get(self,request):
        f = WeatherModels.objects.all()
        ser = WeatherSerializers(f,many=True)
        l = ser.data
        print(l)
        for i in l:
            Qnum = i['Qnum']
            City = i['City']
            text = weather_query(City)
            se.delay(Qnum,str(text),City)

        return Response(status=200)
