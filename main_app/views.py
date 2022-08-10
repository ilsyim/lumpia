from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Lumpia
  
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
  fields = '__all__'

class LumpiaUpdate(UpdateView):
  model = Lumpia
  fields = "__all__"

class LumpiaDelete(DeleteView):
  model = Lumpia
  success_url = '/lumpias/'