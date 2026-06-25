from django.db import models
from django.db.models import CharField


# Create your models here.
class admindata(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(primary_key=True, max_length=100)
    phone = models.IntegerField()
    def __str__(self):
        return self.name

class logindata(models.Model):
    email=models.CharField(max_length=100)
    password=models.IntegerField()
    usertype=models.CharField(max_length=100)
    def __str__(self):
        return self.email

class userdata(models.Model):
    userid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField()
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Cardata(models.Model):
    id = models.AutoField(primary_key=True)
    Car_Name=models.CharField(max_length=100)
    Price_Per_Day=models.IntegerField()
    Car_Model=models.CharField(max_length=100)
    Car_Number=models.CharField(max_length=100)
    Fuel_Type=models.CharField(max_length=100)
    Transmissio=models.CharField(max_length=100)
    Seating_Capacity=models.IntegerField()
    Availability_Status=models.CharField(max_length=100)
    def __str__(self):
        return self.Car_Name

class carphotos(models.Model):
    carid = models.IntegerField()
    Car_Name = models.CharField(max_length=100)
    Car_Photo = models.ImageField(upload_to='cars/')
    def __str__(self):
        return self.Car_Name

class AddToCart(models.Model):
    userid = models.CharField(max_length=100)
    carid = models.IntegerField()
    Car_Photo = models.CharField(max_length=255)
    Car_Name = models.CharField(max_length=100)
    Price_Per_Day = models.IntegerField()
    Car_Model = models.CharField(max_length=100)
    Car_Number = models.CharField(max_length=100)
    Fuel_Type = models.CharField(max_length=100)
    Seating_Capacity = models.IntegerField()
    Added_Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.userid)

class BookNow(models.Model):
    bookingid=models.AutoField(primary_key=True)
    userid=models.CharField(max_length=100)
    Car_Name = models.CharField(max_length=100)
    Car_Number = models.CharField(max_length=100)
    Full_Name = models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    driver_license=models.CharField(max_length=100)
    deicer_license_Photo=models.ImageField(upload_to='cars/')
    Pickup_Date=models.DateField()
    Pickup_Time=models.TimeField()
    Return_Date=models.DateField()
    Return_Time=models.TimeField()
    Pickup_Location=models.CharField(max_length=100)
    Drop_Location=models.CharField(max_length=100)
    Status = models.CharField(max_length=20,default='Pending')
    def __str__(self):
        return self.Full_Name


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)

    Amount = models.IntegerField()
    Payment_Method = models.CharField(max_length=50)
    Payment_Status = models.CharField(max_length=50,default='Pending')
    Transaction_Date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.Amount)