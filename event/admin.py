from django.contrib import admin
from .models import Event,CustomUser,Round1,Round2

admin.site.register([Event,CustomUser,Round1,Round2])