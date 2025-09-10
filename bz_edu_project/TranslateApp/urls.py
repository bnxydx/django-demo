from django.urls import path
from .views import TranslateView
urlpatterns = [
    path('Translate/',TranslateView.as_view()),
]