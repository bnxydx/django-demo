from django.urls import path
from .views import YololistView
urlpatterns = [
    path('yolo/',YololistView.as_view()),
]