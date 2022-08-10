from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Lumpia, Dessert
  
# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def lumpias_index(request):
  lumpias = Lumpia.objects.all()
  return render(request, 'lumpias/index.html', {'lumpias': lumpias})

def lumpias_detail(request, lumpia_id):
  lumpia = Lumpia.objects.get(id=lumpia_id)
  return render(request, 'lumpias/detail.html', { 'lumpia': lumpia })

class LumpiaCreate(CreateView):
  model = Lumpia
  fields = ['protein', 'fillings', 'review']

class LumpiaUpdate(UpdateView):
  model = Lumpia
  fields = '__all__'

class LumpiaDelete(DeleteView):
  model = Lumpia
  success_url = '/lumpias/'

class DessertCreate(CreateView):
  model = Dessert
  fields = '__all__'

class DessertList(ListView):
  model = Dessert

class DessertDetail(DetailView):
  model = Dessert

class DessertUpdate(UpdateView):
  model = Dessert
  fields = '__all__'

class DessertDelete(DeleteView):
  model = Dessert
  success_url = '/desserts/'
