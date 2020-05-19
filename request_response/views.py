from django.shortcuts import render
from django import http
from django.views import View
import json
# Create your views here.
class QSParamView(View):
    """测试提取查询参数字符串
    http://127.0.0.1:8000/querystring/?name=温海辉&age=120
    """

    def get(self,request):
        # 获取查询字符串参数，name,age
        name = request.GET.get('name','小明')
        age = request.GET.get('age','18')

        return http.HttpResponse('查询字符串参数，%s--%s'%(name,age))


class FormDataParamView(View):
    """用于提取表单类型请求体参数
    http://127.0.0.1:8000/formdata/
    """

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        return http.HttpResponse('表单类型请求体参数,%s--%s'%(username,password))


class JSONParamView(View):
    """测试提取非标单类型请求体参数
     http://127.0.0.1:8000/json/
    """

    def post(self,request):
        # 获取请求体中原始的JSON数据
        json_str = request.body
        # 使用json板块见原始的json数据转化为字典
        json_dict = json.loads(json_str)

        # 获取JSON的数据中的参数
        username = json_dict.get('username')
        password = json_dict.get('password')

        return http.HttpResponse('非标单类型请求体参数，%s--%s'%(username,password))


class URLParamView(View):
    """测试path()提取普通路径参数：
    http://127.0.0.1:8000/url_param1/18/
    """

    def get(self,request,age):
        """
        :param request:
        :param age: 路由提取的关键词参数
        :return:
        """

        return http.HttpResponse('测试path()提取普通路径参数：%s'%age)


class URLParam2View(View):
    """测试path()提取普通路径参数：
        http://127.0.0.1:8000/url_param1/18388882222/
    """

    def get(self,request,phonenum):
        """
        :param request:
        :param phonenum: 路由提取的关键词参数
        :return:
        """

        return http.HttpResponse('测试path()提取普通路径参数：%s'%phonenum)


class URLParam3View(View):
    """测试re_path()提取路径参数
    http://127.0.0.1:8000/url_param3/18500001111/
    """

    def get(self, request, phonenum):
        """
        :param phonenum: 路由提取的关键字参数
        """
        return http.HttpResponse('测试re_path()提取路径参数：%s' % phonenum)


