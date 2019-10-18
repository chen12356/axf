from django.db import models

# Create your models here.
#INSERT INTO axf_wheel (id, img, name, trackid) VALUES (1, '/media/images/ad02.jpg', '酸奶女王', 21870);
#建模型-->根据表来 建
class Axf_wheel(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()
    class Meta:
        db_table = 'axf_wheel'

#INSERT INTO axf_nav (id, img, name, trackid) VALUES (1, '/media/images/banner16.jpg', '每日必抢', 21851);
class Axf_nav(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()
    class Meta:
        db_table = 'axf_nav'

#INSERT INTO axf_mustbuy (id, img, name, trackid) VALUES (1, '/media/images/ad01.jpg', '酸奶女王', 21870);
class Axf_mustbuy(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()
    class Meta:
        db_table = 'axf_mustbuy'

"""
INSERT INTO axf_mainshow (id, img, name, trackid, categoryid, brandname, img1, 
childcid1, productid1, longname1, price1, marketprice1, img2, childcid2,
 productid2, longname2, price2, marketprice2, img3, childcid3, productid3, 
 longname3, price3, marketprice3) VALUES (1, '/media/images/ad01.jpg', '优选水果',
  21782, 103532, '爱鲜蜂', '/media/images/goods002.jpg', 103533, 118824, 
  '爱鲜蜂·特小凤西瓜1.5-2.5kg/粒', 25.8, 25.8, '/media/images/goods003.jpg', 
  103534, 116950, '蜂觅·越南直采红心火龙果350-450g/盒', 15.3, 15.8, 
  '/media/images/goods010.jpg', 103533, 118826, '爱鲜蜂·海南千禧果400-450g/盒', 
  9.9, 13.8);
"""
class Axf_mainshow(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()
    categoryid = models.IntegerField()
    brandname = models.CharField(max_length=32)
    img1 = models.CharField(max_length=256)
    childcid1 = models.IntegerField()
    productid1 = models.IntegerField()
    longname1 = models.CharField(max_length=256)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()
    img2 = models.CharField(max_length=256)
    childcid2 = models.IntegerField()
    productid2 = models.IntegerField()
    longname2 = models.CharField(max_length=256)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()
    img3 = models.CharField(max_length=256)
    childcid3 = models.IntegerField()
    productid3 = models.IntegerField()
    longname3 = models.CharField(max_length=256)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()
    class Meta:
        db_table = 'axf_mainshow'
