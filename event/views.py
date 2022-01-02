from django.http import HttpResponse
from django.shortcuts import render
from .models import Event, CustomUser, Round1, Round2
from django.utils import timezone
# Models and Decorators
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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

@login_required
def game(request):
    user = request.user
    customuser = CustomUser.objects.get_or_create(user=request.user)
    if  customuser[0].qualifiedround1 == False and customuser[0].qualifiedround2 == False:

        # Round 1 event logic goes here

        return render(request, "round1.html")
    elif customuser[0].qualifiedround1 == True and customuser[0].qualifiedround2 == False:

        # Round 2 event logic goes here

        return render(request, "round2.html")
    else:

        # Send message via HTML to user to be redy for non website rounds

        return render(request, "userwait.html")

    return HttpResponse("You can see disss")