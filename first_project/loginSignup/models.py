from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(("bio"))
    location = models.CharField(("location"), max_length=50)
    birth_date = models.DateField(("birth day"), auto_now=False, auto_now_add=False)


    
