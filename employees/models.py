from django.db import models

# Create your models here.
class employee(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    employees_id=models.IntegerField()

    def __str__(self):
        return self.first_name

