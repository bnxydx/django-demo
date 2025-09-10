from django.urls import path
from .views import FarToolCategoryView,FarToolCategoryNumView,ToolListCreateView,ToolRetrieveUpdateDestroyView

urlpatterns = [
    path('categories/', FarToolCategoryView.as_view()),
    path('categories/<int:pk>/', FarToolCategoryNumView.as_view()),
    path('tools/', ToolListCreateView.as_view()),
    path('tools/<int:pk>/', ToolRetrieveUpdateDestroyView.as_view()),
]