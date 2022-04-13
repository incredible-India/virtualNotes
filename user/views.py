from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from django.views import View
from . import models
from . import middleware 
from myNotes.models import Categories
import datetime
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
    




#creating new category  form validation code ..
@(middleware.verification)
def newCategory(request):
    if request.method == 'POST':
        if request.isverified:
            #getting data fromthe user side ...
            
            cname = request.POST.get('cname')
            cimg = request.FILES.get('cimg',None)


            #checking the category name in dbs thst already exist or not    

            isExist = Categories.objects.filter(Q(name = cname) & Q(uid = models.User.objects.get(email=request.email)))

            
            
            if cname == '' or len(cname) == 0:
                messages.error(request,'Category name cannot be empty')
                return HttpResponseRedirect('/mynotes/profile/')

            
            elif isExist.exists():
                messages.error(request,'Category name already exists, please choose another name.')
                return HttpResponseRedirect('/mynotes/profile/')

            
            

            else:
                email =  request.email 

                Categories.objects.create(uid = models.User.objects.get(email=email), name = cname , cimg = cimg , dateOf = datetime.datetime.now()).save()


            return HttpResponseRedirect('/mynotes/profile/')
            
        else:
            return HttpResponseRedirect('/user/login/')
    else:
        return HttpResponse('<h1> Somethong went wrong please try again </h1>')