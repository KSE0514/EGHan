from django.db import models
from django.conf import settings

# Create your models here.
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='product_user')


class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts,on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()

    def __str__(self):
        return f'{self.fin_prdt_cd} , {self.intr_rate_type_nm}, {self.intr_rate2}'


class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='savingproduct_user')


class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts,on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()

    def __str__(self):
        return f'{self.fin_prdt_cd} , {self.intr_rate_type_nm}, {self.intr_rate2}'