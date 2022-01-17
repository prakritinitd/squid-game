from django.contrib import admin
from .models import Event,CustomUser,Round1,Round2
from django.utils.html import format_html

class CustomUserAdminPanel(admin.ModelAdmin):
    list_display = ('user','phone','gameover','qualifiedround1','qualifiedround2',)

class Round1AdminPanel(admin.ModelAdmin):
    list_display= ('customuser','started','ended','attempt','passed','gameover','cheater')

class Round2AdminPanel(admin.ModelAdmin):
    
    def image(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image.short_description = 'Image'

    list_display= ('customuser','started','ended','shape','image','uploaded','passed')

admin.site.register(CustomUser,CustomUserAdminPanel)
admin.site.register(Round1,Round1AdminPanel)
admin.site.register(Round2,Round2AdminPanel)
admin.site.register(Event)