from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=120)
    jobrole = models.CharField(max_length=50)

    def __str__(self):
        return self.name