#Django 
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

#Models
from django.contrib.auth.models import User
from users.models import Profile

def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dash')
        else: 
            return render(request, 'users/login.html', {'error' : 'Usuario o Contraseña Invalidos'})
    

    return render(request, 'users/login.html')


def signup_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error' : 'Las contraseñas no coinsiden'})


        user = User.objects.create_user(username=username, password=password)

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.position = request.POST['position']

        user.save()
        
        profile = Profile(user=user)
        profile.save()

        return redirect('login')



    return render(request, 'users/signup.html') 