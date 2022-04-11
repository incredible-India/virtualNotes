from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from user import middleware
from user import models
from django.contrib import messages
from django.db.models import Q
from django.views import View
from django.utils.decorators import method_decorator
# Create your views here.
@(middleware.verification)
def index(request):
    #first checking the user authentications 
    if request.isverified:
        
        userName = request.name
        userinfo =  models.User.objects.get(email=request.email)

        userimage = userinfo.image
        return render(request,'myNotes/profile.html',
        {'uname':userName,'email':request.email,'lname' : request.lname,
         'userimage' : userimage})
    else:
        return HttpResponseRedirect('/user/login/')





#creating the sticky notes.....

class crtStickyNotes(View):
    @method_decorator(middleware.verification)
    def get(self, request):
        if request.isverified:
            uname = request.name
            return render(request,'myNotes/Crtsticky.html',{
                'uname' : uname
            })
        else:
            return HttpResponseRedirect('/user/login/')

    @method_decorator(middleware.verification)
    def post(self, request):
        if request.isverified:
            data =  request.POST.get('notes')

            return HttpResponse(data)
        else:
            return HttpResponseRedirect('/user/login/')
        
        

