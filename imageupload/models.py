from django.db import models

# Create your models here.

class Hotel(models.Model):
   
    hotel_Main_Img = models.ImageField(upload_to='media')
    class Meta:
        db_table=('Hotel')


class Hotel1(models.Model):
   
    hotel_Main_Img1 = models.ImageField(upload_to='media')
    class Meta:
        db_table=('Hotel1')

class Hotel2(models.Model):
   
    hotel_Main_Img2 = models.ImageField(upload_to='media')
    class Meta:
        db_table=('Hotel2')

class Hotel3(models.Model):
   
    hotel_Main_Img3 = models.ImageField(upload_to='media')
    class Meta:
        db_table=('Hotel3')

class Hotel4(models.Model):
   
    hotel_Main_Img4 = models.ImageField(upload_to='media')
    class Meta:
        db_table=('Hotel4')

