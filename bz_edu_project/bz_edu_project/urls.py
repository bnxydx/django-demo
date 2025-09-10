from . import views  # 导入视图
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    # path("index", views.index, name="index"),
    # path("", LoginView.as_view()),  # 添加首页路由
    path("admin/", admin.site.urls),
    path("api/", include('user_app.url')),
    path("",include('yoloapp.urls')),
    path("",include('dwrg.urls')),
    path("",include('tools.urls')),
    path("", include('TranslateApp.urls')),

]


from django.conf import settings

# 添加媒体文件的URL配置
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.RUNS_URL, document_root=settings.RUNS_ROOT)
else:
    # 生产环境下也需要提供媒体文件访问
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.RUNS_URL, document_root=settings.RUNS_ROOT)