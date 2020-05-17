from django.shortcuts import render
from django import http
from django.views import View
# Create your views here.


class RegisterView(View):

    def get(self,request):
        """
        处理GET请求，返回注册页面
        :param request: 请求对象，包含请求报文信息
        :return: 响应对象，用于构建响应报文，并响应给用户
        """
        return http.HttpResponse("温海辉注册页面！")

    def post(self,request):
        """
        处理post请求，返回注册逻辑页面
        :param request: 请求对象，包含请求报文信息
        :return: 响应对象，用于构建响应报文，并响应给用户
        """
        return http.HttpResponse("温海辉注册逻辑页面")


# def register(request):
#     """
#     用户注册函数视图
#     :param request: 请求对象，包含了请求报文。request
#     :return: 响应对象，用于构造响应报文并且返回给用户
#     """
#     return http.HttpResponse("温海辉注册页面！")
