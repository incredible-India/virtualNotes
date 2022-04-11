from . import models


class verification:
    def __init__(self,get_response):
        self.get_response = get_response

    
    def __call__(self,request):
        email = request.session.get('userAuth',None)
     
        checkInDBS =  models.User.objects.filter(email=email)

        
        if email == None :
            request.isverified = False

        elif len(checkInDBS) == 0:

            request.isverified = False
        
        
        else:
            request.isverified = True
            request.email = email
            userName =  models.User.objects.get(email=request.email)
            request.name =  userName.fname
       
        
        response = self.get_response(request)    
        return response