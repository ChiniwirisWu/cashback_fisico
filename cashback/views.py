from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models
import json

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

#
def add_to_budget(request):
    print(request.body)
    body = json.loads(request.body)
    amount = body['amount']
    user_hash = body['user_hash']
    print(amount)
    try:
        target = models.User.objects.get(user_hash = user_hash)
        #add 0.09%
        target.budget += round(float(amount) * 0.09, 2)
        target.save()
        return HttpResponse(200)
    except models.User.DoesNotExist:
        return HttpResponse(404)

def add_to_budget(request):
    body = json.loads(request.body)
    amount = body['amount']
    user_hash = body['user_hash']
    if(user_hash == ''):
        return HttpResponse(404)
    try:
        target = models.User.objects.get(user_hash = user_hash)
        #add 0.09%
        target.budget += round(float(amount) * 0.09, 2)
        target.save()
        return HttpResponse(200)
    except models.User.DoesNotExist:
        return HttpResponse(404)

def remove_from_budget(request):
    body = json.loads(request.body)
    amount = body['amount']
    user_hash = body['user_hash']
    print(body)
    if(user_hash == ''):
        print('hi')
        return HttpResponse(404)
    try:
        target = models.User.objects.get(user_hash = user_hash)
        #add 0.09%
        target.budget -= float(amount)
        if(target.budget >= 0):
            target.save()
            return HttpResponse(200)
        else:
            return HttpResponse(404)
    except models.User.DoesNotExist:
        return HttpResponse(404)

