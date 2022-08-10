from re import template
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Lumpia, Dessert
from django.contrib.auth.views import LoginView

# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def lumpias_index(request):
  lumpias = Lumpia.objects.all()
  return render(request, 'lumpias/index.html', {'lumpias': lumpias})

def lumpias_detail(request, lumpia_id):
  lumpia = Lumpia.objects.get(id=lumpia_id)
  desserts_not_added = Dessert.objects.exclude(id__in = lumpia.desserts.all().values_list('id'))
  return render(request, 'lumpias/detail.html', { 'lumpia': lumpia, 'desserts': desserts_not_added })

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

def assoc_dessert(request, lumpia_id, dessert_id):
  Lumpia.objects.get(id=lumpia_id).desserts.add(dessert_id)
  return redirect('lumpias_detail', lumpia_id=lumpia_id)