"""Django_base_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,register_converter
from converters import MobileConverter

# 注册自定义路由转换器
# register_converter(自定义路由转换器,'别名')
register_converter(MobileConverter, 'mobile')

urlpatterns = [
    # 自带的后台管理系统的总路由，可以忽略
    path('admin/', admin.site.urls),

    # 总路由包含子路由的语法
    # path('网络地址前缀/',include('子应用.urls')),
    # 或者 path('',includes('子应用.urls')),

    # 用户模块：http://127.0.0.1/users/register/
    path('',include('users.urls')),

    # 请求与响应
    path('',include('request_response.urls'))
]
