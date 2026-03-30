from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=40)
    standard = models.IntegerField()
    place = models.CharField(max_length=50)