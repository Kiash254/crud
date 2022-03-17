from django.db import models

# Create your models here.
class Port(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    age=models.IntegerField(null=True)
    career=models.CharField(max_length=50,null=True)
    tribe=models.CharField(max_length=50,null=True)
    hobbies=models.CharField(max_length=50,null=True)
    talent=models.CharField(max_length=50,null=True)
    def __str__ (self):
        return f'age{self.age},career{self.tribe},hobbies{self.hobbies}'
    
