from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class TrustFund(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="trustfund")
    fullname = models.CharField(max_length=255)
    card_id = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
