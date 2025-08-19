from rest_framework import serializers

from .models import Course, Stage, Chapter, Section


class CourseListSerializer(serializers.ModelSerializer):
    '''
   课程分类序列化器
   '''
    stage_count = serializers.IntegerField()
    chapter_count = serializers.IntegerField()
    section_count = serializers.IntegerField()
    class Meta:
        model = Course
        fields = '__all__'


class StageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'


class ChapterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class SectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class ChapterDetailSerializer(serializers.ModelSerializer):
    '''
     课程章节详情序列化器
     '''
    # 课程章节下的所有小节
    sections = SectionListSerializer(many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = '__all__'


class StageDetailSerializer(serializers.ModelSerializer):
    '''
     课程阶段详情序列化器
     '''
    # 课程阶段下的所有章节
    chapters = ChapterDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Stage
        fields = '__all__'
