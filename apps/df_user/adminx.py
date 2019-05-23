# -*-coding:utf-8-*-
# _author_ = without
# _Date_ = 2019/5/8
# _Time_ = 23:41
# _IDE_ = PyCharm
import io
import sys

from django.contrib import admin
import xadmin
from .models import UserInfo, GoodsBrowser

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

class UserInfoAdmin(object):
    list_display = ["uname", "uemail", "ushou", "uaddress", "uyoubian", "uphone","upwd"]
    list_per_page = 5
    list_filter = ["uname", "uyoubian",]
    search_fields = ["uname", "uyoubian"]
    readonly_fields = ["uname"]


class GoodsBrowserAdmin(object):
    list_display = ["user", "good"]
    list_per_page = 50
    list_filter = ["user__uname", "good__gtitle"]
    search_fields = ["user__uname", "good__gtitle"]
    readonly_fields = ["user", "good"]
    refresh_times = [3, 5]


xadmin.site.site_header = u'天天生鲜后台管理系统'
xadmin.site.site_title = u'天天生鲜后台管理系统'

xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(GoodsBrowser, GoodsBrowserAdmin)