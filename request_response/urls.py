from django.views import View
from django import http
from django.urls import path,include
from . import views


urlpatterns = [
    # 测试提取查询字符串参数：http://127.0.0.1:8000/querystring/?name=zxc&age=18
    path('querystring/', views.QSParamView.as_view()),
    # 测试提取表单类型请求体数据：http://127.0.0.1:8000/formdata/
    path('formdata/', views.FormDataParamView.as_view()),
    # 测试提取非表单类型请求体参数 json---http://127.0.0.1:8000/json/
    path('json/', views.JSONParamView.as_view()),
    # 测试path()提取普通路径参数：http://127.0.0.1:8000/url_param1/18/
    path('url_param1/<int:age>/', views.URLParamView.as_view()),
    #测试path()提取普通路径参数：http://127.0.0.1:8000/url_param1/18388882222/
    path('url_param1/<mobile:phonenum>/', views.URLParam2View.as_view()),
    #测试path()提取普通路径参数：http://127.0.0.1:8000/url_param1/18388882222/
    path(r'^url_param1/(?P<phonenum>1[3-9]\d{9})/$', views.URLParam3View.as_view()),

]

