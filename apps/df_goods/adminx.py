<<<<<<< HEAD
# -*-coding:utf-8-*-
# _author_ = without
# _Date_ = 2019/5/9
# _Time_ = 14:14
# _IDE_ = PyCharm
# superuser: root 123123...
from django.contrib import admin
import xadmin
from .models import TypeInfo, GoodsInfo


# 注册模型类  普通方法
@xadmin.sites.register(TypeInfo)
class TypeInfoAdmin(object):
    list_display = ['id', 'ttitle']
    list_per_page = 10
    list_filter = ['ttitle']
    search_fields = ['ttitle']
    list_display_links = ['ttitle']

@xadmin.sites.register(GoodsInfo)
class GoodsInfoAdmin(object):
    list_per_page = 20
    list_display = ['id', 'gtitle', 'gunit', 'gclick', 'gprice', 'gpic', 'gkucun', 'gjianjie','gmin','gkeep','gstock']
    list_filter = ['gkucun', 'gclick']
    list_editable = ['gkucun', ]
    readonly_fields = ['gclick']
    search_fields = ['gtitle', 'gcontent', 'gjianjie']
    list_display_links = ['gtitle']

# xadmin.site.register(TypeInfo, TypeInfoAdmin)
# xadmin.site.register(GoodsInfo, GoodsInfoAdmin)
=======
import xadmin
from .models import TypeInfo, GoodsInfo

class TypeInfoAdmin:
    list_display = ['id', 'ttitle']
    list_per_page = 10
    search_fields = ['ttitle']
    list_display_links = ['ttitle']


class GoodsInfoAdmin:
    list_per_page = 20
    list_display = ['id', 'gtitle', 'gunit', 'gclick', 'gprice', 'gpic', 'gkucun', 'gjianjie','gmin','gkeep','gstock']
    list_editable = ['gkucun','gmin','gkeep','gstock' ]
    readonly_fields = ['gclick']
    search_fields = ['gtitle', 'gcontent', 'gjianjie']
    list_display_links = ['gtitle']
    list_filter = ['id', 'gtitle', 'gunit', 'gclick', 'gprice', 'gpic', 'gkucun', 'gjianjie','gmin','gkeep','gstock']


xadmin.site.register(TypeInfo, TypeInfoAdmin)
xadmin.site.register(GoodsInfo, GoodsInfoAdmin)

>>>>>>> 179e61dbddb0904127c8715edb6e9a1cf02e0095
