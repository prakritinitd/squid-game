from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Event, CustomUser, Round1, Round2
from django.utils import timezone
# Models and Decorators
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

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
    customuser = CustomUser.objects.get_or_create(user=user)
    auth0user = user.social_auth.get(provider='auth0')

    if customuser[0].gameover == True:
        return render(request,"Gameover.html")

    if  customuser[0].qualifiedround1 == False and customuser[0].qualifiedround2 == False:
        round1 = Round1.objects.filter(user=user).first()
        if round1 == None:
            round1 = Round1(user=user,customuser=customuser[0])
            round1.save()
        return render(request, "round1.html",{'auth0User':auth0user})
    elif customuser[0].qualifiedround1 == True and customuser[0].qualifiedround2 == False:

        # Round 2 event logic goes here

        return render(request, "round2.html")
    else:

        # Send message via HTML to user to be ready for non website rounds

        return render(request, "userwait.html")

    return HttpResponse("You can see disss")

@login_required
def attemptsLeftRound1(request):
    round1 = Round1.objects.get(user=request.user)
    return JsonResponse({"message": 3 - round1.attempt})

@login_required
def replayRoundOne(request):
    print("REPLAY CALLED !")
    USER = request.user
    customUser = CustomUser.objects.get(user=USER)
    round1 = Round1.objects.get(user=USER)
    if round1.attempt <=2 and round1.gameover == False:
        round1.attempt += 1 
        round1.save()
    if round1.attempt == 3: # Therefore total no of attempts are 2 only
        if round1.ended is None :
            round1.ended = timezone.now()
            round1.gameover = True
            customUser.gameover = True
            customUser.save()
            round1.save()
        return JsonResponse({"status": False,"HelpText": "Your no. of attempts are over, thus Jayeon's Squid Game is over for you"})
    return JsonResponse({"status": True,"HelpText": "Try moving your head sideways to achieve greater speed, This is your last attempt play wisely"})

@login_required
def SuccessRound1(request):
    if request.method == 'POST':
        USER = request.user
        round1 = Round1.objects.get(user=USER)
        customUser = CustomUser.objects.get(user=USER)
        attempt = round1.attempt
        if customUser.gameover == True:
            return JsonResponse({"message": "Game over !"})
        elif round1.ended is not None:
            return JsonResponse({"message": "Game over !"})
        elif attempt == 3:
            return JsonResponse({"message": "Game over !"})
        elif attempt == 1 or attempt == 2:
            customUser.qualifiedround1 = True
            round1.passed = True
            round1.ended = timezone.now()
            round1.save()
            customUser.save()
            return JsonResponse({"message": "Congratulations you are promoted to the next round which will begin in 30 minutes be ready!"})