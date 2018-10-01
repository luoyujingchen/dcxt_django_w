from django.urls import path
from testapp.views import upload_img


urlpatterns = [
    path('uploadImg/', upload_img), #新增
]