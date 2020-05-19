from django.shortcuts import render
from django import http
from django.views import View
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