from django.urls import path
from .views import upload_file,GetFileView
urlpatterns = [
    path('upload_file/',upload_file.as_view()),
    path('get_file/<int:pk>/', GetFileView.as_view()),

]