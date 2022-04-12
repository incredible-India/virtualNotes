import re
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from user import middleware
from user import models
from django.contrib import messages
from django.db.models import Q
from django.views import View
from django.utils.decorators import method_decorator
from .models import StickyNotes
from user.models import User
import datetime
import os 
from gtts import gTTS
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
            #sending the sticky notes which is saved in dbs.. only six 
            stckynts = StickyNotes.objects.filter(userid = User.objects.get(email = request.email))
            
            return render(request,'myNotes/Crtsticky.html',{
                'uname' : uname
                ,
                'data' : stckynts
            })
        else:
            return HttpResponseRedirect('/user/login/')


    @method_decorator(middleware.verification)
    def post(self, request):
        if request.isverified:
            data =  request.POST.get('notes')

            #saving the notes coming from user in database 

            if len(data) == 0 or data == '':
                messages.error(request,'Blank Notes Cannot Be Saved..')
                return HttpResponseRedirect('/mynotes/crt/sticky/notes/')
            
            else:
                userid = User.objects.get(email=request.email)
                saveInDBS = StickyNotes.objects.create(userid=userid,textIs = str(data) ,dateOf = datetime.datetime.now())

                messages.success(request,'data saved successfully')
              
                return HttpResponseRedirect('/mynotes/crt/sticky/notes/')



            
        else:
            return HttpResponseRedirect('/user/login/')
        
        

#particular notes delete sticky notes.. in create sticky notes page..


def deleteStickyNote(request,id):
    if request.session.get('userAuth',None) != None:
        
        deleteIt = StickyNotes.objects.filter(id = id)

        if len(deleteIt) == 0:
            return HttpResponse('<h1> Something Went Wrong </h1>')
        
        else:
            StickyNotes.objects.get(id=id).delete()
            messages.success(request,'successfully Notes Deleted')
            return HttpResponseRedirect('/mynotes/all/saticky/')

    else:
        return HttpResponseRedirect('/user/login/')
    

#for showing all the page of sticky notes

@(middleware.verification)
def showAllStickyNotes(request):
    if request.isverified:
        uname = request.name
 
        stckynts = StickyNotes.objects.filter(userid = User.objects.get(email = request.email))
        return render(request,'myNotes/allSticky.html',{
            'uname':uname,
        'data': stckynts
        })



    else:
        return HttpResponseRedirect('/user/login/')

    

#delete all the sticky notes in show all sticky page..

@(middleware.verification)
def DeleteAllStickyNotes(request):
    if request.isverified:
        uname = request.name
 
        stckynts = StickyNotes.objects.filter(userid = User.objects.get(email = request.email))

        stckynts.delete()

        return HttpResponseRedirect('/mynotes/all/saticky/')



    else:
        return HttpResponseRedirect('/user/login/')


    


#this routing is in audio formate of sticky notes 
@(middleware.verification)
def speechNotesRouting(request):
    if request.isverified:
        email = request.email
        toSpeech =  StickyNotes.objects.filter(userid = User.objects.get(email = email))
        #first we save all the data in notes in the txt file 
        with open('stcknotes.txt','w') as writeIn:
            for i in toSpeech:
                writeIn.write(f'On Date {i.dateOf} the notes is {i.textIs}\n \n')

        #reading the saved data from txtfile 'stcknotes.txt' 

        with open('stcknotes.txt.','r') as readText:
            
            textToSpeech = readText.read()

            if textToSpeech == '':
                textToSpeech = 'NO Notes Available'
        
        #now write the code for gtts 

        speechOBJ =  gTTS(text = str(textToSpeech), lang='hi', slow=False)

        speechOBJ.save('speack.mp3')

        os.system('speack.mp3')

        os.remove('speack.mp3')

        os.remove('stcknotes.txt')

        

            
        
        return render(request,'myNotes/textToSpeech.html',{
            'uname' : request.name
        })

    else:
        return HttpResponseRedirect('/user/login/')
 