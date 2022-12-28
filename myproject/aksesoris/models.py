from django.db import models

# Create your models here.
class aksesorisModel(models.Model):
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=200)


    def __str__(self):
        return "{}.{}". format(self.id, self.email)