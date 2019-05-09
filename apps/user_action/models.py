from django.db import models
from df_user.models import UserInfo
from df_goods.models import GoodsInfo
from datetime import datetime
# Create your models here.


class UserComment(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="用户ID")
    good = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="商品ID")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="评论时间")
    comment = models.TextField(max_length=1000, verbose_name="评论内容")

    class Meta:
        verbose_name = "用户评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}用户评论".format(self.user.uname)