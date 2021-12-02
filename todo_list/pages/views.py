from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Todo
from django.urls import reverse_lazy
# Create your views here.
class HomePageView(ListView):
    model = Todo
    template_name = 'home.html'

class HomeDetailView(DetailView):
    model = Todo
    template_name = 'detail.html'

class HomeCreateView(CreateView):
    model = Todo
    template_name = 'todo_new.html'
    fields = ['body']

class HomeUpdateView(UpdateView):
    model = Todo
    template_name = 'todo_edit.html'
    fields = ['body']

class HomeDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('home')