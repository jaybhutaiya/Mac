from django.db import models

# Create your models here.
class emplloye(models.Model):
    empname=models.CharField(max_length=20)
    empno=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.empname
    
class leave(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField()
    email=models.EmailField()
    message=models.CharField(max_length=20)

    def __str__(self):
        return self.name  
      
class course(models.Model):
    image=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=200)
    duration=models.CharField(max_length=200)
    bi=models.ImageField(upload_to='images/')
    cname=models.CharField(max_length=200)
    cinfo=models.CharField(max_length=400)
    cimg=models.ImageField(upload_to='images/')
    cname1=models.CharField(max_length=200,default='None')
    cinfo1=models.CharField(max_length=400,default='None')
    cimg1=models.ImageField(upload_to='images/',default='None')
    
    def __str__(self):
        return self.name