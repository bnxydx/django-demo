from django.urls import path
from .views import TeacherListViews
urlpatterns = [
    path('teachers/',TeacherListViews.as_view()),

]