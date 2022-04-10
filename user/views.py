from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from django.views import View
from . import models
from . import middleware 
#external module 

# from cryptography.fernet import Fernet # encryption and decryption text

# Create your views here.
# nEW USER GETTING FROM DATA 
@(middleware.verification)
def newUser(request):

    if request.isverified == False :


        if request.method == 'POST':
        #getting the form data  
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            image = request.FILES['image']
            password = request.POST.get('password')
            cnfpassword = request.POST.get('cnfpassword')
        
        
        #validating the form data

            if len(fname) < 2 and len(lname) < 2 :
                messages.error(request,'First name and Last name should be more than 3 characters long..')
                return render(request,'user/newuser.html') 
            elif password != cnfpassword:
                messages.error(request,'Password and confirm password does not matched..')
                return render(request,'user/newuser.html') 
        #checking the email exist or not in database or not 

            isExistEmail =  models.User.objects.filter(email = email)

            if len(isExistEmail) != 0:
                messages.error(request,'Email already exist, if you have already an account please go for log in.')
                return render(request,'user/newuser.html') 
        
            else:
            #savig the user information in the database.. 

                saveInDBS  = models.User.objects.create(fname=fname, email=email,lname=lname,password=password,image=image)
                saveInDBS.save()

            #seting the session for the user authentication 
            # key = Fernet.generate_key()
 
            # # Instance the Fernet class with the key
 
            # fernet = Fernet(key)

            # encMessage = fernet.encrypt(b'email') #data must be in bytes

            # print(email,encMessage)

                request.session['userAuth'] = email

            # decMessage = fernet.decrypt(encMessage).decode()

                return HttpResponseRedirect('/')


        else:
            return render(request,'user/newuser.html')
    
    else:
        return HttpResponseRedirect('/')






#user login routing code
@(middleware.verification)
def login(request):

    if request.isverified == False:
    
        if request.method == 'POST':
            email =  request.POST.get('email')
            password = request.POST.get('password')

        #checking the information in database 

            isExist = models.User.objects.filter( Q(email=email) & Q(password = password))

            if len(isExist) == 0:
                messages.error(request,'Incorrect details.')
              
                return render(request,'user/login.html')
        
            else:
                request.session['userAuth'] = email
                return HttpResponseRedirect('/')
    
        else:


            return render(request,'user/login.html')
    
    else:
            return HttpResponseRedirect('/')




#for the logout routing  function
@(middleware.verification)
def logout(request):
    if request.isverified :
        del request.session['userAuth']

        return HttpResponseRedirect('/')
    
    else: 
        return HttpResponseRedirect('/')
    