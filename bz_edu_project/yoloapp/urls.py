from django.urls import path
from .views import YoloListView

urlpatterns = [
    path('yolo/',YoloListView.as_view())
]