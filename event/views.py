from django.http import HttpResponse
from django.shortcuts import render
from .models import Event
from django.utils import timezone

def home(request):
    auth0user = {}
    
    event = Event.objects.filter().first()
    if event == None :
        return HttpResponse("<h1>No Event Happening Right Now</h1>")
    else:
        now = timezone.now()
        status = None
        if event.start > now:
            # Coming Soon
            status = -1
        if event.start < now and event.end > now:
            # Event ongoing
            status = 0
        if now > event.end:
            # Event Ended
            status = 1
        
        if request.user.is_authenticated:
            user = request.user
            auth0user = user.social_auth.get(provider='auth0')

        return render(request, "index.html", {'auth0User': auth0user,'status':status})
        