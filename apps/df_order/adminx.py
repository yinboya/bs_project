<<<<<<< HEAD
# -*-coding:utf-8-*-
# _author_ = without
# _Date_ = 2019/5/8
# _Time_ = 23:39
# _IDE_ = PyCharm
from django.contrib import admin

=======
>>>>>>> 179e61dbddb0904127c8715edb6e9a1cf02e0095
import xadmin
from .models import OrderDetailInfo, OrderInfo


<<<<<<< HEAD
@xadmin.sites.register(OrderInfo)
class OrderInfoAdmin(object):
=======
class OrderInfoAdmin:
>>>>>>> 179e61dbddb0904127c8715edb6e9a1cf02e0095

    list_display = ["oid", "user", "odate", "ototal", "oaddress"]
    list_per_page = 5
    list_filter = ["user", "odate", "oaddress"]
    search_fields = ["user__uname"]
    ordering = ["-odate"]


<<<<<<< HEAD
@xadmin.sites.register(OrderDetailInfo)
class OrderDetailInfoAdmin(object):
=======
class OrderDetailInfoAdmin:
>>>>>>> 179e61dbddb0904127c8715edb6e9a1cf02e0095

    list_display = ["goods", "order", "price", "count"]
    list_per_page = 5
    list_filter = ["goods"]
<<<<<<< HEAD
=======




xadmin.site.register(OrderInfo, OrderInfoAdmin)
xadmin.site.register(OrderDetailInfo, OrderDetailInfoAdmin)

>>>>>>> 179e61dbddb0904127c8715edb6e9a1cf02e0095
