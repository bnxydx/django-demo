from django.urls import path
from .views import students,student
# from .tmp import students,student
from .APIview_practice import StudentList,StudentDetail
urlpatterns = [
    path('students/',StudentList.as_view()),
    path('student/<int:id>/',StudentDetail.as_view()),
]