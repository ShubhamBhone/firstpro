from django.db import models

# Create your models here.
class Studentdata(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.IntegerField()
    marks=models.FloatField()

    def __str__(self):
        return self.name
