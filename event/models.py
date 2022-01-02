from django.db import models
from django.contrib.auth.models import User, AbstractUser
import random

class Event (models.Model):
    name = models.CharField(verbose_name="Event Name",max_length=100)
    start = models.DateTimeField(verbose_name=("Event Starting Time"),)
    end = models.DateTimeField(verbose_name=("Event Starting Time"),)

    def __str__(self):
        return self.name

class CustomUser (models.Model):
    user = models.OneToOneField(User,verbose_name=("User"), on_delete=models.CASCADE,null=True)
    score = models.SmallIntegerField(default=0)
    qualifiedround1 = models.BooleanField(default=False,verbose_name=("Qualified Round 1 ?"),null=True)
    qualifiedround2 = models.BooleanField(default=False,verbose_name=("Qualified Round 2 ?"),null=True)

    def __str__(self):
        return self.user.first_name
    

class Round1 (models.Model):
    user = models.OneToOneField(User,verbose_name=("User"), on_delete=models.CASCADE)
    customuser = models.OneToOneField(CustomUser,verbose_name=("Custom User"), on_delete=models.CASCADE,editable=False,null=True)
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    started = models.DateTimeField(verbose_name="Started Time")
    ended = models.DateTimeField("Ended Time")
    cheater = models.BooleanField(default=False,null=True)
    passed = models.BooleanField(default=False,null=True)

class Round2 (models.Model):

    def randomize():
        shapes = ['heart','crescent','star','umbrella']
        return shapes[random.randint(0, 3)]

    user = models.OneToOneField(User,verbose_name=("User"), on_delete=models.CASCADE)
    customuser = models.OneToOneField(CustomUser,verbose_name=("Custom User"), on_delete=models.CASCADE,editable=False,null=True)
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    started = models.DateTimeField(verbose_name="Started Time")
    ended = models.DateTimeField("Ended Time")
    cheater = models.BooleanField(default=False,null=True)
    passed = models.BooleanField(default=False,null=True)

    shape = models.CharField(verbose_name="Shape Assigned",max_length=10,default=randomize())
    image = models.ImageField(upload_to="uploads/")