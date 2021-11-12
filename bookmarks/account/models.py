from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField

class Profile(models.Model):
    user = OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_urodzenia = models.DateField(blank=True, null=True)
    zdjęcie = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return "Profil użytkownika {}.".format(self.user.username)
