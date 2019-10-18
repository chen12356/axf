from django.db import models

# Create your models here.
from MarketApp.models import Axf_goods
from UserApp.models import Axf_user

# 创建关联表的模型
class Axf_cart(models.Model):
    c_goods = models.ForeignKey(Axf_goods)
    c_user = models.ForeignKey(Axf_user)
    c_goods_num = models.IntegerField(default=1)
    # 默认选中
    c_is_select = models.BooleanField(default=True)
    class Meta:
        db_table = 'axf_cart'