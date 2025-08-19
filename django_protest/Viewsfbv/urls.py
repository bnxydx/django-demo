from django.urls import path
from .views import  *

urlpatterns=[
    path('fbv/',fbv_function),
    path('cbv/', CBVview.as_view()),
    path('args_index/',index),

]