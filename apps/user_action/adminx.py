<<<<<<< HEAD
# -*-coding:utf-8-*-
# _author_ = without
# _Date_ = 2019/5/11
# _Time_ = 10:51
# _IDE_ = PyCharm
from django.contrib import admin

=======
>>>>>>> 179e61dbddb0904127c8715edb6e9a1cf02e0095
import xadmin
from .models import UserComment


<<<<<<< HEAD
# 注册模型类  普通方法
class UserCommentAdmin(object):
    list_display = ['user', 'good', 'add_time', 'comment']
    list_per_page = 10
    search_fields = ['user', 'good', 'add_time', 'comment']
    list_display_links = ['user', 'good', 'add_time', 'comment']


xadmin.site.register(UserComment, UserCommentAdmin)
# admin.site.register(GoodsInfo.gkucun, GoodsInfoAdmin)
=======

class UserCommentAdmin:
    list_display = ['user','add_time','comment']
    search_fields = ['user', 'comment']
    list_filter = ['user', 'add_time', 'comment']


xadmin.site.register(UserComment, UserCommentAdmin)
>>>>>>> 179e61dbddb0904127c8715edb6e9a1cf02e0095
