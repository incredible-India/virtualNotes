
from django.urls import path,include
from . import views as uv
from user import urls

urlpatterns = [
 
    path('newUser/',uv.newUser,name='newusers'),
    path('login/',uv.login,name='login'),
    path('logout/',uv.logout,name='logiout'),
    path('check/validation/category/',uv.newCategory,name='newcategoris'),
]
