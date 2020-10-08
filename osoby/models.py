from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Klasa(models.Model):
    nazwa = models.CharField("nazwa klasy", max_length=4, default="")
    rok_matury = models.IntegerField("rok matury", default=0)
    rok_naboru = models.IntegerField("rok naboru", default=0)

    class Meta:
        verbose_name_plural = 'klasy'

    def __str__(self):
        return self.nazwa

class Absolwent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    klasa = models.ForeignKey(Klasa, on_delete=models.SET_NULL, blank=True, null=True)
