from django.urls import path
from .views import RotationChartView
urlpatterns = [
    path('Rete/',RotationChartView.as_view())
]
