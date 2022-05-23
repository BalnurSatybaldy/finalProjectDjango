from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    charity = models.OneToOneField("charity.Charity", on_delete=models.CASCADE)
    number_of_members = models.IntegerField(default=0)
    members = models.ManyToManyField(User)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
