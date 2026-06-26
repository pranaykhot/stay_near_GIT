from django.db import models


# Create your models here.
class AdminMaster(models.Model):
    ad_id = models.AutoField(primary_key=True, unique=True)
    ad_name = models.CharField(max_length=100)
    ad_mobile = models.CharField(max_length=100)
    ad_email = models.CharField(max_length=100)
    ad_password = models.CharField(max_length=100)
    ad_role = models.CharField(max_length=100)
    ad_status = models.IntegerField(default=0)
    ad_created_by = models.CharField(max_length=100, default="")


class AddVendors(models.Model):
    av_id = models.AutoField(primary_key=True, unique=True)
    av_name = models.CharField(max_length=100)
    av_mobile = models.CharField(max_length=100)
    av_email = models.CharField(max_length=100)
    av_password = models.CharField(max_length=100)
    av_role = models.CharField(max_length=100)
    av_status = models.IntegerField(default=0)
    av_created_by = models.CharField(max_length=100, default="")


class AddPG(models.Model):
    ab_id = models.AutoField(primary_key=True, unique=True)
    ab_name = models.CharField(max_length=100)
    ab_price = models.CharField(max_length=100)
    ab_details = models.CharField(max_length=100)
    ab_address = models.CharField(max_length=100, default="")
    ab_location = models.TextField(max_length=100, default="")
    ab_image = models.ImageField(upload_to="app/static/media/pg/")
    ab_status = models.IntegerField(default=0)
    ab_created_by = models.CharField(max_length=100, default="")


class Register(models.Model):
    rg_id = models.AutoField(primary_key=True, unique=True)
    rg_name = models.CharField(max_length=100)
    rg_mobile = models.CharField(max_length=100)
    rg_email = models.CharField(max_length=100)
    rg_password = models.CharField(max_length=100)
    rg_address = models.CharField(max_length=100, default="")
    rg_status = models.CharField(max_length=100, default="0")


class Contact(models.Model):
    ct_id = models.AutoField(primary_key=True, unique=True)
    ct_name = models.CharField(max_length=100)
    ct_mobile = models.CharField(max_length=100)
    ct_email = models.CharField(max_length=100)
    ct_subject = models.CharField(max_length=100)
    ct_message = models.CharField(max_length=100, default="")
    ct_status = models.CharField(max_length=100, default="0")


class Order(models.Model):
    or_id = models.AutoField(primary_key=True, unique=True)
    or_name = models.CharField(max_length=100)
    or_total_amount = models.CharField(max_length=100)
    or_address = models.CharField(max_length=100)
    or_ordered_by = models.CharField(max_length=100)
    or_transaction_id = models.CharField(max_length=100)
    or_status = models.CharField(max_length=100, default=0)
    or_created_by = models.CharField(max_length=100)


class Review(models.Model):
    rv_id = models.AutoField(primary_key=True, unique=True)
    rv_pg_id = models.CharField(max_length=100, default="")
    rv_name = models.CharField(max_length=100)
    rv_mobile = models.CharField(max_length=100)
    rv_email = models.CharField(max_length=100)
    rv_review = models.CharField(max_length=100, default="")
    rv_status = models.CharField(max_length=100, default="0")


class ForgotPassword(models.Model):
    fp_id = models.AutoField(primary_key=True, unique=True)
    fp_email = models.CharField(max_length=100, default="")
    fp_otp = models.CharField(max_length=100, default="")
