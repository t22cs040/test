from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class UserData(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    password = models.CharField(validators=[MinLengthValidator(10)], max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name