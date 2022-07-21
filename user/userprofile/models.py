from django.db import models

# Create your models here.
class user(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    email = models.EmailField(blank=True)
    phoneNumber= models.CharField(max_length=12)

    def __str__(self):
        return self.firstname 


class Employer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    isAdmin = models.BooleanField()
    userId = models.ForeignKey(user,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name
