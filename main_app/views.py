from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')