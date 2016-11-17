from __future__ import unicode_literals

from django.db import models
import bcrypt
# Create your models here.

class UserManager(models.Manager):

    def register(self,data):

        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']

        errors=[]

        # print email, first_name, last_name
        if data['pwd'] == data['pwd2']:
            # encrypt password
            # put stuff in  front of .Create
            temp = data['pwd']
            hashed = bcrypt.hashpw(temp,bcrypt.gensalt())
            user = models.User.objects.create(email=email, first_name=first_name, last_name=last_name, password=hashed)
            return (True, user)
        else:
            return (False, errors)

    def login(self,**kwargs):
        pass

class User(models.Model):
    email = models.EmailField(max_length = 100, null = False)
    password = models.CharField(max_length = 255 )
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
