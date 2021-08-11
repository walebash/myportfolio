from django.db import models
from django.db.models import DateField, CharField
from django.core.validators import RegexValidator

# Create your models here.

class Client(models.Model):
    phoneNumberRegex = RegexValidator(regex= r"^\+?1?\d{8,15}$")
    client_name = models.CharField(max_length=200)
    client_email = models.CharField(max_length=100)
    client_phone = models.CharField(validators = [phoneNumberRegex], max_length= 16, unique= True)
    date_published = models.DateField(blank = True, null = True)