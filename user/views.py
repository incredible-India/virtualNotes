from django.shortcuts import render

# Create your views here.

def newUser(request):
    return render(request,'user/newuser.html')



def login(request):
    return render(request,'user/login.html')