from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,ListView,TemplateView
from app.models import *
# Create your views here.



class NoteCreateView(CreateView):
    model = Note
    template_name = "index.html"
    success_url = 'success/'
    fields=('body',)





class NoteListView(ListView):
    model = Note
    template_name = "all_note.html"
    fields = ('body',)


class success(TemplateView):
    template_name = "sucess.html"


class deleted(TemplateView):
    template_name = "deleted.html"


class edited(TemplateView):
    template_name = "edited.html"

class NoteDeleteView(DeleteView):
    model = Note
    success_url = 'deleted/'
    template_name = "confirm_delete.html"




class NoteUpdateView(UpdateView):
    model = Note
    template_name = "edit.html"
    success_url='edited/'
    fields = ('body',)




