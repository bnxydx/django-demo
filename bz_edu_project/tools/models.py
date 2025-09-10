from django.db import models

# Create your models here.
class FarToolCategory(models.Model):  # 更清晰的名字
    name = models.CharField(max_length=100, verbose_name='工具总类名字')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_far_tool_category'  # 推荐下划线命名
        verbose_name = '工具大类'
        verbose_name_plural = '工具大类'


class Tool(models.Model):
    name = models.CharField(max_length=100, verbose_name='工具名称')
    description = models.CharField(max_length=100, verbose_name='工具描述',null=True)  # 建议拆分
    url = models.URLField(max_length=1000, verbose_name='跳转链接')  # 用 URLField 更好
    category = models.ForeignKey(
        FarToolCategory,
        on_delete=models.CASCADE,
        related_name='tools'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_tool'
        verbose_name = '工具'
        verbose_name_plural = '工具'
