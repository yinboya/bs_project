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
    list_filter = ['gkeep']


xadmin.site.register(TypeInfo, TypeInfoAdmin)
xadmin.site.register(GoodsInfo, GoodsInfoAdmin)

