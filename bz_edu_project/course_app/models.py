from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='课程分类名称')
    learn_info = models.CharField(blank=True, null=True, max_length=255, verbose_name='课程学习信息')
    learn_style = models.CharField(blank=True, null=True, max_length=255, verbose_name='课程学习方式')
    learn_time = models.CharField(blank=True, null=True, max_length=255, verbose_name='课程学习时间')
    supervision = models.CharField(blank=True, null=True, max_length=255, verbose_name='课程监督方式')
    icon = models.CharField(blank=True, null=True, max_length=255, verbose_name='课程分类图标')
    brief = models.CharField(blank=True, null=True, max_length=255, verbose_name='课程分类简介')
    level = models.IntegerField(blank=True, null=True, verbose_name='课程分类级别')

    class Meta:
        db_table = 't_course'


class Stage(models.Model):
    '''
   课程阶段表
   '''
    name = models.CharField(max_length=255, verbose_name='课程阶段名称')
    introduction = models.CharField(blank=True, null=True, max_length=255, verbose_name='课程阶段简介')
    level = models.IntegerField(blank=True, null=True, verbose_name='课程阶段级别')
    is_free = models.IntegerField(blank=True, null=True, verbose_name='是否免费')

    course = models.ForeignKey(Course, related_name='stages', on_delete=models.CASCADE, verbose_name='课程分类',
                               null=True, blank=True)

    class Meta:
        db_table = 't_stage'


class Chapter(models.Model):
    '''
     课程章节表
     '''
    name = models.CharField(max_length=255, verbose_name='课程章节名称')
    level = models.IntegerField(blank=True, null=True, verbose_name='课程章节级别')

    stage = models.ForeignKey(Stage, related_name='chapters', on_delete=models.CASCADE, verbose_name='课程阶段',
                              null=True, blank=True)

    class Meta:
        db_table = 't_chapter'


class Section(models.Model):
    '''
     课程小节表
     '''
    name = models.CharField(max_length=255, verbose_name='课程小节名称')
    is_must = models.IntegerField(blank=True, null=True, verbose_name='是否必修')
    duration = models.IntegerField(blank=True, null=True, verbose_name='课程时长')
    learned_count = models.IntegerField(blank=True, null=True, verbose_name='学习人数')
    url = models.CharField(blank=True, null=True, max_length=255, verbose_name='课程小节视频地址')
    chapter = models.ForeignKey(Chapter, related_name='sections', on_delete=models.CASCADE, verbose_name='课程章节',
                                null=True, blank=True)

    class Meta:
        db_table = 't_section'
