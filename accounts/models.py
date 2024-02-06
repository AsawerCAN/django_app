from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here. #AUTH_USER_MODEL is define in core settings

class CustomUser(AbstractUser): #AbstractUser inherit which make easy to ad custom fields 
    GENDER_CHOICES= [
        ('M', 'Male' ),
        ('F', 'Female' ),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    

    