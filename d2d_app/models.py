from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, primary_key=True)                   # Unique ref to djangos user model
    bankAccountNo = models.PositiveIntegerField(null=True, blank=True)
    bankRoutingNo = models.PositiveIntegerField(null=True, blank=True)
    def email(self):
        return self.user.username     
    def __str__(self):
        return self.user.username
        
class Package(models.Model):
    description = models.TextField()
    price = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    length = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    def shipping_price(self):
        return 1000.0*pow(0.01,3.0)*(self.height*self.width*self.length)
    def __str__(self):
        return self.description

class Driver(models.Model):
    driverID = models.PositiveIntegerField(primary_key=True)
    def __str__(self):
        return str(self.driverID)

class Contract(models.Model):

    seller = models.ForeignKey(Customer, related_name='seller')
    package = models.ForeignKey(Package, unique=True, blank=True)    
    buyer = models.ForeignKey(Customer, related_name='buyer')
    
    payed = models.BooleanField(default=False)
    buyerSatisfied = models.BooleanField(default=False) 
    settled = models.BooleanField(default=False)
    def __str__(self):
        return "Contract: " + self.package.description

