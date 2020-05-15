from django.urls import path

# 导入需要配置路径路由的文件
from . import views

urlpatterns = [
    # 函数视图路由语法
    # path('网络地址枕着表达式',函数视图名)

    # 用户注册的地址是http://127.0.0.1/users/register/
    path('users/register/',views.register)
]


