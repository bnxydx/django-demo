from django.urls import path
from .views import students,student,classes_detail
# from .tmp import students,student
from .APIview_practice import StudentList,StudentDetail
from .views import index

urlpatterns = [
    path('students/',StudentList.as_view()),
    # path('students/',index),
    path('course/<int:pk>/',classes_detail),
    path('student/<int:id>/',StudentDetail.as_view()),
]