from django.contrib import admin
from .models import UserComment


# 注册模型类  普通方法
class UserCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'good', 'add_time', 'comment']
    list_per_page = 10
    search_fields = ['user', 'good', 'add_time', 'comment']
    list_display_links = ['user', 'good', 'add_time', 'comment']

admin.site.register(UserComment, UserCommentAdmin)
# admin.site.register(GoodsInfo.gkucun, GoodsInfoAdmin)
