from django.shortcuts import render,redirect,reverse
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


class Response1View(View):
    """测试HttpResponse
    http://127.0.0.1:8000/response1/
    """

    def get(self, request):
        # 使用HttpResponse构造响应数据
        # return http.HttpResponse(content='itcast python', status=200)
        # 可简写
        # return http.HttpResponse('itcast python')

        # 另外一种写法
        response = http.HttpResponse('itcast python')
        return response


class JSONResponseView(View):
    """测试HttpResponse
    http://127.0.0.1:8000/json_resp/
    """

    def get(self,request):
        # 准备相应数据
        dict_data = {
            'city':'beijing',
            'subject':'python'
        }
        # 使用JsonResponse构造并返回json数据
        return http.JsonResponse(dict_data)


class IndexView(View):
    """测试重定向首页
    http://127.0.0.1:8000/index/
    """

    def get(self,request):
        return http.HttpResponse('这是一个重定向之后首页')


class LoginReditectView(View):
    """测试重定向转化页面前
    http://127.0.0.1:8000/login_redirect/
    """

    def post(self,request):
        # 假装正在处理登录逻辑处理
        # 假装登录逻辑处理完成

        # 通过用户重定向引导到首页
        # return redirect('/index/')

        # ret_url = reverse('总路由别名：子路由别名')
        ret_url = reverse('request_response:index')
        return redirect(ret_url)



