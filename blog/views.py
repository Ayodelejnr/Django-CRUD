from cgitb import html
from pyexpat import model
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .models import blogApp

class blogAppCreateView(CreateView):
    model= blogApp
    fields= [
        "title",
        "description"
    ]
    template_name = 'base.html'
    success_url = "post_list.html"



class blogAppListView(ListView):
     model = blogApp
     template_name = 'post_list.html'


class blogAppDetailView(DetailView):
    model = blogApp
    template_name = 'post_detail.html'


class blogAppUpdateView(UpdateView):
    model = blogApp
    fields =[
        "title",
        "description"
    ]
    template_name = 'post_update.html'
    success_url = '/'


class bolgAppDeleteView(DeleteView):
    model = blogApp
    template_name = 'post_confirm_delete.html'
    success_url = '/'
