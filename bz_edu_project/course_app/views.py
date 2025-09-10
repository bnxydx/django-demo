from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics
from .models import Course, Stage, Section, Chapter
from rest_framework.pagination import PageNumberPagination
from .serializers import CourseListSerializer, StageListSerializer, ChapterListSerializer, SectionListSerializer, \
    StageDetailSerializer


# Create your views here.
class LargeResultsSetPagiation(PageNumberPagination):
    page_size = 2  # 默认每页显示多少条数据
    max_page_size = 10  # 前端在控制每页显示多少条时，最多不能超过10
    page_query_param = 'page'  # 前端在查询字符串的关键字 指定显示第几页的名字，不指定默认时page
    page_size_query_param = 'page_size'  # 前端在查询字符串的关键字名字，是用来控制每页显示多少条的关键字


class ResultsSetPagination(PageNumberPagination):
    '''
   自定义分页器
   '''
    page_query_param = 'page'
    page_size_query_param = 'size'
    page_size = 10


class CourseListView(generics.ListAPIView):
    # queryset = Course.objects.all()
    queryset = Course.objects.annotate(
        stage_count=Count('stages'),
        chapter_count=Count('stages__chapters'),
        section_count=Count('stages__chapters__sections')
    ).values(
        'id', 'name', 'learn_info', 'learn_style', 'learn_time', 'supervision', 'icon', 'brief', 'level',
        'stage_count', 'chapter_count', 'section_count',
    )
    serializer_class = CourseListSerializer

    # 设置分页器
    pagination_class = ResultsSetPagination


class StageListView(generics.ListAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageListSerializer

    # 设置是数据过滤器
    filterset_fields = ('course',)  # 多个 根据外键


class ChapterListView(generics.ListAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterListSerializer

    filterset_fields = ('stage',)  # 多个 根据外键


class SectionListView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionListSerializer
    filterset_fields = ('chapter',)  # 多个 根据外键


class StageDetailView(generics.RetrieveAPIView):  # RetrieveAPIView找单一的某一个数据区别
    queryset = Stage.objects.all()
    serializer_class = StageDetailSerializer
