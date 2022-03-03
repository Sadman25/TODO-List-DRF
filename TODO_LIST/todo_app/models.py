from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class todoList(models.Model):
    task = models.CharField(max_length=100,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.task
