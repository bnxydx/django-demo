from django.urls import path
from .views import ToolsView
urlpatterns = [
    path("tools/", ToolsView.as_view()),
    path("tools/<int:pk>/", ToolsView.as_view()),
]