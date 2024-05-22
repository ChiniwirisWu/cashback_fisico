from django.shortcuts import render
from . import models

# Create your views here.
def view_login(request):
    return render(request, 'login.html', context={})

def view_register(request):
    return render(request, 'register.html', context={})

def view_user(request):
    return render(request, 'user.html', context={})

def view_admin(request):
    return render(request, 'admin.html', context={})

#functionalities
def create_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = models.User.objects.get(username=username)
        return render(request, 'register.html', context={'msg':'username already taken.'})
    except models.User.DoesNotExist:
        user = models.User(username=username, password=password, category='user')
        user.save()
        user_hash = hash(str(user.id))
        user.user_hash = user_hash
        user.save()
        return render(request, 'login.html', context={'msg':'user created succesfully!'})

#
def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = models.User.objects.get(username=username, password=password)
        user.state = 1
        if(user.category == 'admin' and user.state == 1):
            return render(request, 'admin.html', context={'user':user})
        elif(user.category == 'user' and user.state == 1):
            return render(request, 'user.html', context={'user':user})
        else:
            return render(request, 'login.html', context={})
    except models.User.DoesNotExist:
        return render(request, 'login.html', context={'msg':'username or password incorrect.'})
#
def logout_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = models.User.objects.get(username=username, password=password)
        user.state = 0
        return render(request, 'login.html', context={})
    except models.User.DoesNotExist:
        return render(request, 'login.html', context={})



