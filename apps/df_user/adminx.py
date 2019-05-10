__author__ = 'xumeng'
__date__ = '2018/7/3 17:05'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord

from .models import UserInfo, GoodsBrowser
# from user_action.models import UserComment



class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = '天天生鲜商城后台系统'
    site_footer = '天天生鲜商城'
    menu_style = 'accordion'

class UserInfoAdmin:
    list_display = ["uname", "uemail", "ushou", "uaddress", "uyoubian", "uphone","upwd"]
    list_per_page = 5
    list_filter = ["uname", "uyoubian",]
    search_fields = ["uname", "uyoubian"]
    readonly_fields = ["uname"]


class GoodsBrowserAdmin:
    list_display = ["user", "good"]
    list_per_page = 50
    list_filter = ["user__uname", "good__gtitle"]
    search_fields = ["user__uname", "good__gtitle"]
    readonly_fields = ["user", "good"]
    refresh_times = [3, 5]

class EmailVerifyRecordAdmin:
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['email', 'code']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    # 设置图标
    model_icon = 'fa fa-codiepie'

xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(GoodsBrowser, GoodsBrowserAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)



xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
