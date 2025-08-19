from django.urls import path
from .views import request_index
urlpatterns = [
    path('request/',request_index),

]