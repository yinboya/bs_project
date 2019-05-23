#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *

app_name = 'df_user'

urlpatterns = [
    url(r'^register/$', register, name="register"),
    url(r'^register_handle/$', register_handle, name="register_handle"),
    url(r'^register_exist/$', register_exist, name="register_exist"),
    url(r'^login/$', login, name="login"),
    url(r'^login_handle/$', login_handle, name="login_handle"),
    url(r'^info/$', info, name="info"),
    url(r'^order/(\d+)$', order, name="order"),
    url(r'^site/$', site, name="site"),
    # url(r'^place_order/$', views.place_order),
    url(r'^logout/$', logout, name="logout"),
    url(r'^password/$', password, name="password"),  # 渲染页面
    url(r'^password_exist/$', password_exist, name="password_exist"),  # 验证用户名是否存在
    url(r'^password_1/$', password_1, name="password_1"),  # 对用户名和邮箱进行验证
    url(r'^password_again/$', password_again, name="password_again"),  # 用户修改密码
    url(r'^password_jiu/$', password_jiu, name="password_jiu"),  # 验证旧密码

]