from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    community = models.CharField(default= '')
    updated_at = models.DateTimeField(auto_now=True)