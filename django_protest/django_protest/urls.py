from django.contrib import admin
from django.urls import path,include
from user.views import login_form, get_user, index
from request_app.views import request_index, upload_image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("login/", login_form),
    path("getuser/<id>/", get_user),
    path("request/", request_index),
    path("upload/", upload_image, name="upload_image"),  # 添加图片上传路由
    path("api/",include("student_api.urls")),
    path("", include("Viewsfbv.urls")),
    path("",include("fileapp.urls")),
    path("", include("yoloapp.urls")),

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

# polls是子应用
handler404 = "user.views.page_not_found"