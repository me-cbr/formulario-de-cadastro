from django.db import models


class Register(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)