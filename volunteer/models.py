from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="donations")
    charity = models.ForeignKey("charity.Charity", on_delete=models.CASCADE, related_name="donations")
    price = models.FloatField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)


class Volunteering(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="volunteering")
    charity = models.ForeignKey("charity.Charity", on_delete=models.CASCADE, related_name="volunteers")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="volunteer")
    phone_number = PhoneNumberField(null=True, blank=True, default="+77779185334")
