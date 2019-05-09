from django.shortcuts import render
from .models import UserComment
from df_goods.models import GoodsInfo
from df_user.models import UserInfo
from django.http import JsonResponse
from df_user import user_decorator
import json
# Create your views here.


@user_decorator.login
def add_comment(request):
    if request.method == "POST":
        user_id = request.session['user_id']
        good_id = request.POST.get("goods_id")
        comment = request.POST.get("comment")
        if UserComment.objects.filter(user=user_id, good=good_id):
            return JsonResponse({"code": 0, "msg": "您已经评论过了"})
        else:
            comment_obj = UserComment()
            comment_obj.user_id = int(user_id)
            comment_obj.good_id = int(good_id)
            comment_obj.comment = comment
            comment_obj.save()
            return JsonResponse({"code": 1, "msg": "添加成功"})