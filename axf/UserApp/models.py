from django.db import models

# Create your models here.

class Axf_user(models.Model):
    u_name = models.CharField(max_length=32)
    u_password = models.CharField(max_length=256)
    u_email = models.CharField(max_length=64)
    u_icon = models.ImageField(upload_to='icons')
    # 设置状态,默认是未激活,需要使用邮箱验证才可
    u_active = models.BooleanField(default=False)
    #设置一个字段,用来存取一个混淆串,作为参数传递
    u_token = models.CharField(max_length=256)

    class Meta:
        db_table = 'axf_user'