from django.urls import path
from .views import WeatherView,SubscribeWeatherView,SendWeatherData
urlpatterns = [
    path('weather/',WeatherView.as_view()),
    path('weatherSub/',SubscribeWeatherView.as_view()),
    path('weatherSend/',SendWeatherData.as_view())
]