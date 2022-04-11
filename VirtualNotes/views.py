from django.shortcuts import HttpResponse,render
from user import middleware


@(middleware.verification)
def index(request):

    if request.isverified == False:
        login =False
        uname = 'User'
    else:
        login = True
        uname = request.name

    return render(request,'index.html',{'login':login,'uname' : uname})