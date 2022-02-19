from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    landmark = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=100)
    pincode = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username + 'Address'
