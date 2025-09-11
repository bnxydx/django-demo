from django.urls import path
from .views import ClientListView,ClientAddView, data_visualization_view, data_upload_view
urlpatterns = [
    path("list/",ClientListView.as_view()),
    path("add/", ClientAddView.as_view()),
    path("visualization/", data_visualization_view, name='data_visualization'),
    path("upload/", data_upload_view, name='data_upload'),
]
