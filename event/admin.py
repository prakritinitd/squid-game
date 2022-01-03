from django.contrib import admin
from .models import Event,CustomUser,Round1,Round2

class CustomUserAdminPanel(admin.ModelAdmin):
    list_display = ('user','score','gameover','qualifiedround1','qualifiedround2',)

class Round1AdminPanel(admin.ModelAdmin):
    list_display= ('customuser','started','ended','attempt','passed','gameover','cheater')


admin.site.register(CustomUser,CustomUserAdminPanel)
admin.site.register(Round1,Round1AdminPanel)
admin.site.register([Event,Round2])