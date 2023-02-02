from django.urls import path
from app.views import *

urlpatterns = [
    path('',NoteCreateView.as_view(),name='home'),
    path('note', NoteListView.as_view(), name='notes'),
    path('success/',success.as_view(),name='success'),
    path('<pk>/delete/deleted/', deleted.as_view(), name='deleted'),
    path('<pk>/edit/edited/', edited.as_view(), name='edited'),


    path('<pk>/delete/', NoteDeleteView.as_view(),name='delete'),
    path('<pk>/edit/', NoteUpdateView.as_view(), name='edit'),



]
