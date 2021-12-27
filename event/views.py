from django.shortcuts import render


def home(request):
    auth0user = {}
    
    if request.user.is_authenticated:
        user = request.user
        auth0user = user.social_auth.get(provider='auth0')
        userdata = {
            'user_id': auth0user.uid,
            'name': user.first_name,
            'picture': auth0user.extra_data['picture'],
            'email': auth0user.extra_data['email'],
        }
    return render(request, "index.html", {'auth0User': auth0user})
    