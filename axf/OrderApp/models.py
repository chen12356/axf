from django.db import models

# Create your models here.

# 设置模型，此时应有订单表、订单商品表
# 知道订单表和用户表是关系，多对一，
# 在订单商品表和商品表肯定有关系，一对多
from MarketApp.models import Axf_goods
from UserApp.models import Axf_user


class Axf_order(models.Model):
    # 和用户有关系，那么加个关联
    o_user = models.ForeignKey(Axf_user)
    o_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'axf_order'

class Axf_order_goods(models.Model):
    # 订单商品表，注意和谁有关系，那么就设对于的外键，后面查询数据好查
    og_order = models.ForeignKey(Axf_order)

    #页面展示用这个 模型去去展示
    og_goods = models.ForeignKey(Axf_goods)

    og_goods_num = models.IntegerField()
    og_price = models.FloatField()
    class Meta:
        db_table = 'axf_order_goods'