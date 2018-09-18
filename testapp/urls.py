from django.urls import path

from testapp.views import uploadImg

urlpatterns = [
    path('uploadImg/', uploadImg), # 新增
]