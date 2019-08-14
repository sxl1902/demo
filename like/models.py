from django.db import models

# Create your models here.
class Like(models.Model):
    uid = models.ImageField()
    time = models.DateTimeField()
    xxx = models.CharField()