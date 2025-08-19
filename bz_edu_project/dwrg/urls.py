from django.urls import path
from .views import DwrgVIew
urlpatterns = [
    path('dwrg/',DwrgVIew.as_view()),
]