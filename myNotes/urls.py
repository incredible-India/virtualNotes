
from . import views as mv

from django.urls import path,include


urlpatterns = [
 
    path('profile/',mv.index,name='profile'),
    path('crt/sticky/notes/',mv.crtStickyNotes.as_view(),name='stickyNotes')

]
