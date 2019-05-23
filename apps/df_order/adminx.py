# -*-coding:utf-8-*-
# _author_ = without
# _Date_ = 2019/5/8
# _Time_ = 23:39
# _IDE_ = PyCharm
from django.contrib import admin

import xadmin
from .models import OrderDetailInfo, OrderInfo


@xadmin.sites.register(OrderInfo)
class OrderInfoAdmin(object):

    list_display = ["oid", "user", "odate", "ototal", "oaddress"]
    list_per_page = 5
    list_filter = ["user", "odate", "oaddress"]
    search_fields = ["user__uname"]
    ordering = ["-odate"]


@xadmin.sites.register(OrderDetailInfo)
class OrderDetailInfoAdmin(object):

    list_display = ["goods", "order", "price", "count"]
    list_per_page = 5
    list_filter = ["goods"]
