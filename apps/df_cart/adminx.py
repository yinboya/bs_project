# -*-coding:utf-8-*-
# _author_ = without
# _Date_ = 2019/5/8
# _Time_ = 23:25
# _IDE_ = PyCharm
from django.contrib import admin

import xadmin
from .models import CartInfo


@xadmin.sites.register(CartInfo)
class CartInfoAdmin(object):
    list_display = ['user', 'goods', 'count']
    list_per_page = 5
    list_filter = ['user', 'goods', 'count']
    search_fields = ['user_uname', 'goods__gtitle']
    readonly_fields = ['user', 'goods', 'count']

# class CartInfoAdmin:
#     list_display = ['user', 'goods', 'count']
#     search_fields = ['user_uname', 'goods__gtitle']
#     list_filter = ['user', 'goods', 'count']
#
# xadmin.site.register(CartInfo, CartInfoAdmin)