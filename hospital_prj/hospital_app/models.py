from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.IntegerField()

    def __str__(self):
        return self.name
    