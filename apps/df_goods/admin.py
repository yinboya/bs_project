# superuser: root 123123...
from django.contrib import admin
from .models import TypeInfo, GoodsInfo


# 注册模型类  普通方法
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']
    list_per_page = 10
    search_fields = ['ttitle']
    list_display_links = ['ttitle']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'gtitle', 'gunit', 'gclick', 'gprice', 'gpic', 'gkucun', 'gjianjie','gmin','gkeep','gstock']
    list_editable = ['gkucun','gmin','gkeep','gstock' ]
    readonly_fields = ['gclick']
    search_fields = ['gtitle', 'gcontent', 'gjianjie']
    list_display_links = ['gtitle']
    list_filter = ['gkeep']


admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
# admin.site.register(GoodsInfo.gkucun, GoodsInfoAdmin)
