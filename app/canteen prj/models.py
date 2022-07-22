from django.db import models

# Create your models here.


class Student_table(models.Model):
    Name=models.CharField(max_length=200)
    Phone=models.CharField(max_length=200,unique=True)
    Address=models.CharField(max_length=200)
    Batch=models.CharField(max_length=200)
   
    Username=models.CharField(max_length=200)
    Pswrd=models.CharField(max_length=200)
    Wallet=models.CharField(max_length=200,default="0")



class Canteen_table(models.Model):
    Cname=models.CharField(max_length=200)
    Owname=models.CharField(max_length=200)
    Phone=models.CharField(max_length=200,unique=True)
    Address=models.CharField(max_length=200)
    Username=models.CharField(max_length=200)
    Pswrd=models.CharField(max_length=200)

class Food_table(models.Model):
    Cusername=models.CharField(max_length=200)
    Fname=models.CharField(max_length=200)
    Finfo=models.CharField(max_length=200)
    Price=models.CharField(max_length=200,default="0")
    Time=models.CharField(max_length=200,default="0")
    Date=models.CharField(max_length=200,default="0")
    Ftype=models.CharField(max_length=200,default="0")
    Status=models.CharField(max_length=200,default="0")

class Bucket_table(models.Model):
    Foodid=models.CharField(max_length=200)
    Cusernm=models.CharField(max_length=200,default="0")
    Fname=models.CharField(max_length=200)
    Quantity=models.CharField(max_length=200,default="0")
    Price=models.CharField(max_length=200,default="0")
    Date=models.CharField(max_length=200,default="0")
    Ftype=models.CharField(max_length=200,default="0")
    Sname=models.CharField(max_length=200,default="0")
    
class Purchase_table(models.Model):
    Cusernm=models.CharField(max_length=200)
    Fooditems=models.CharField(max_length=200)
    Quantity=models.CharField(max_length=200)
    Price=models.CharField(max_length=200)
    Total=models.CharField(max_length=200)
    Date=models.CharField(max_length=200)
    Sname=models.CharField(max_length=200)
    Secretid=models.CharField(max_length=200,default="0000")
    Qrpath=models.CharField(max_length=200,default="0000")
    Status=models.CharField(max_length=200,default="Orderd")

# class Notifications(models.Model):
#     uid=models.CharField(max_length=200)
#     date=models.CharField(max_length=200)
#     type=models.CharField(max_length=200,default='0')