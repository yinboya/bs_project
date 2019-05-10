import xadmin

from .models import CartInfo


class CartInfoAdmin:
    list_display = ['user', 'goods', 'count']
    list_per_page = 5
    list_filter = ['user', 'goods', 'count']
    search_fields = ['user_uname', 'goods__gtitle']
    readonly_fields = ['user', 'goods', 'count']


xadmin.site.register(CartInfo,CartInfoAdmin)