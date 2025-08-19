from django.urls import path


from . import views
urlpatterns = [
  path('courses/',views.CourseListView.as_view()),
  path('stages/',views.StageListView.as_view()),
  path('chapters/',views.ChapterListView.as_view()),
  path('sections/',views.SectionListView.as_view()),
  path('stages/<int:pk>/',views.StageDetailView.as_view()),
]
