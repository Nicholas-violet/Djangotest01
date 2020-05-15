from django.shortcuts import render
from django import http
# Create your views here.

def register(request):
    """
    用户注册函数视图
    :param request: 请求对象，包含了请求报文。request
    :return: 响应对象，用于构造响应报文并且返回给用户
    """
    return http.HttpResponse("温海辉注册页面！")
