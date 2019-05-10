import xadmin
from .models import UserComment



class UserCommentAdmin:
    list_display = ['user','add_time','comment']
    search_fields = ['user', 'comment']
    list_filter = ['user', 'add_time', 'comment']
xadmin.site.register(UserComment, UserCommentAdmin)