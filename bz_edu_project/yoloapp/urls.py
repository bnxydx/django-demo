from django.urls import path
from .views import YoloListView, SendEmailView, HistoryDataView, YoloHistoryPageView

urlpatterns = [
    path('yolo/', YoloListView.as_view()),
    path('yolo/send-email/', SendEmailView.as_view()),
    path('yolohistory/', HistoryDataView.as_view()),  # API接口
    path('yolo/history/', YoloHistoryPageView.as_view()),  # 前端页面
]