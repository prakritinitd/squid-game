from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
import random

class Event (models.Model):
    name = models.CharField(verbose_name="Event Name",max_length=100)
    start = models.DateTimeField(verbose_name=("Event Starting Time"),)
    end = models.DateTimeField(verbose_name=("Event Starting Time"),)

    def __str__(self):
        return self.name

class CustomUser (models.Model):
    user = models.OneToOneField(User,verbose_name=("User"), on_delete=models.CASCADE,null=True)
    gameover =  models.BooleanField(default=False,verbose_name=("Game Over"),null=True)
    qualifiedround1 = models.BooleanField(default=False,verbose_name=("Qualified Round 1 ?"),null=True)
    qualifiedround2 = models.BooleanField(default=False,verbose_name=("Qualified Round 2 ?"),null=True)
    phone = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.user.first_name
    

class Round1 (models.Model):
    user = models.OneToOneField(User,verbose_name=("User"), on_delete=models.CASCADE)
    customuser = models.OneToOneField(CustomUser,verbose_name=("Custom User"), on_delete=models.CASCADE,editable=False,null=True)

    started = models.DateTimeField(verbose_name="Started Time",null=True,default=timezone.now)
    ended = models.DateTimeField("Ended Time",null=True,blank= True)

    attempt= models.SmallIntegerField(verbose_name="Attempt Number",default=1,null=True)
    cheater = models.BooleanField("Is A Cheater",default=False,null=True)
    gameover = models.BooleanField("Game Over ",default=False,null=True)
    passed = models.BooleanField(verbose_name="Has Passed This Round",default=False,null=True)

    def __str__(self):
        return self.user.first_name

class Round2 (models.Model):

    user = models.OneToOneField(User,verbose_name=("User"), on_delete=models.CASCADE)
    customuser = models.OneToOneField(CustomUser,verbose_name=("Custom User"), on_delete=models.CASCADE,editable=False,null=True)

    started = models.DateTimeField(verbose_name="Started Time",null=True,default=timezone.now)
    ended = models.DateTimeField("Ended Time",null=True,blank= True)

    uploaded = models.BooleanField(default=False,null=True)
    passed = models.BooleanField(default=False,null=True)

    shape = models.CharField(verbose_name="Shape Assigned",max_length=50,null=True)
    image = models.ImageField(verbose_name="Uploaded Image",upload_to="uploads/",null=True,blank=True)

    def __str__(self):
        return self.user.first_name