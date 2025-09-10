from django.urls import path
from .views import YoloListView, SendEmailView

urlpatterns = [
    path('yolo/', YoloListView.as_view()),
    path('yolo/send-email/', SendEmailView.as_view()),
]