from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
=======
import xadmin
from django.urls import path,re_path
>>>>>>> 179e61dbddb0904127c8715edb6e9a1cf02e0095
from django.conf.urls import url, include
from django.views.static import serve  # 上传文件处理函数
from df_user.views import ForgetPwdView,ResetView,ModifyPwdView
from .settings import MEDIA_ROOT,STATIC_ROOT

<<<<<<< HEAD
import xadmin
from .settings import MEDIA_ROOT
=======
>>>>>>> 179e61dbddb0904127c8715edb6e9a1cf02e0095



urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
=======
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),

>>>>>>> 179e61dbddb0904127c8715edb6e9a1cf02e0095
    url(r'^', include('df_goods.urls', namespace='df_goods')),
    url(r'^user/', include('df_user.urls', namespace='df_user')),
    url(r'^cart/', include('df_cart.urls', namespace='df_cart')),
    url(r'^order/', include('df_order.urls', namespace='df_order')),
    url(r'^user_action/', include('user_action.urls', namespace='user_action')),
    url(r'^tinymce/', include('tinymce.urls')),  # 使用富文本编辑框配置confurl
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
    # 关闭debug模式
    re_path('static/(?P<path>.*)', serve, {'document_root': STATIC_ROOT}),


    # 忘记密码修改
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
]
