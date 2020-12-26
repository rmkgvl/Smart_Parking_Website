from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    address = models.TextField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Parking_area(models.Model):
    admin_id = models.ForeignKey(Admin,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    number_of_parking_slots = models.IntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    base = models.IntegerField()
    tariff = models.FloatField()
    def __str__(self):
        return self.name

#class Parking_slot(models.Model):
#   parking_slot_id = models.IntegerField()
#    parking_area_id = models.ForeignKey(Parking_area,on_delete=models.CASCADE)
#    status = models.BooleanField(default=True)
#    start_time = models.TimeField()
#    end_time = models.TimeField()
#
#    def __str__(self):
#        return self.parking_slot_id

class Orders(models.Model):
    parking_area_id = models.ForeignKey(Parking_area,on_delete=models.CASCADE)
    #parking_slot_id = models.ForeignKey(Parking_slot,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=10)
    starting_time = models.TimeField()
    ending_time = models.TimeField()
    status = models.BooleanField(default=True)
    #date = models.DateField(null=True)