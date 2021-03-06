from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=30 , primary_key = True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()

class Group(models.Model):
    groupid = models.CharField(max_length=30, primary_key = True)
    userid = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

class Authorityinfo(models.Model):
    authorityid = models.CharField(max_length=30, primary_key = True)
    authorityname = models.CharField(max_length=30)

class Memberships(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    authorityinfo = models.ForeignKey(Authorityinfo, on_delete=models.CASCADE,default='')

