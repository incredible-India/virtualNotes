
from . import views as mv

from django.urls import path,include


urlpatterns = [
 
    path('profile/',mv.index,name='profile'),
    path('crt/sticky/notes/',mv.crtStickyNotes.as_view(),name='stickyNotes'),
    path('delete/sticky/<int:id>/',mv.deleteStickyNote,name='DeletestickyNotes'),
    path('all/saticky/',mv.showAllStickyNotes,name='allStickyNotes'),
    path('all/delete/sticky/',mv.DeleteAllStickyNotes,name='allStickyNotesDeleted'),
    path('speech/snotes/',mv.speechNotesRouting,name='spksnts'),

    #now the routing for the making notes  


]
