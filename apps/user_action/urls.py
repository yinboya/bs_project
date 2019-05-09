#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *

app_name = 'user_action'

urlpatterns = [
    url(r'^add_comment/$', add_comment, name="add_comment"),
    # url(r'^register_handle/$', register_handle, name="register_handle"),
    # url(r'^register_exist/$', register_exist, name="register_exist"),
    # url(r'^login/$', login, name="login"),
    # url(r'^login_handle/$', login_handle, name="login_handle"),
    # url(r'^info/$', info, name="info"),
    # url(r'^order/(\d+)$', order, name="order"),
    # url(r'^site/$', site, name="site"),
    # url(r'^logout/$', logout, name="logout"),
]