from django.views import View
from django import http
from django.urls import path,include
from . import views


urlpatterns = [
    # 测试提取查询字符串参数：http://127.0.0.1:8000/querystring/?name=zxc&age=18
    path('querystring/', views.QSParamView.as_view()),
]

