from django.db import models

# Create your models here.
class employee(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    employee_id=models.IntegerField()
    challenge=models.TextField(blank=True,null=True)
    done=models.NullBooleanField(null=True,default=False)
   
    working=models.TextField(blank=True,null=True)
   
    quality_check=models.NullBooleanField(null=True,default=False)

    def __str__(self):
        return self.first_name

