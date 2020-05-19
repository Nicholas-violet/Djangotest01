from django.shortcuts import render
from django import http
from django.views import View
# Create your views here.
class QSParamView(View):
    """测试提取查询参数字符串

    """

    def get(self,request):
        # 获取查询字符串参数，name,age
        name = request.GET.get('name','小明')
        age = request.GET.get('age','18')

        return http.HttpResponse('查询字符串参数，%s--%s'%(name,age))