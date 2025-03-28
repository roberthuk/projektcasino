from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):  
    saldo = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def __str__(self):
        return self.username
