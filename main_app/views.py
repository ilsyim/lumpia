from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Lumpia
  
lumpias = [
  Lumpia('fish', 'noodles and veggies', 'So fresh and so clean'),
  Lumpia('pork', 'glass noodles and veggies', 'Crunchy, best when fried'),
  Lumpia('tofu', 'onions, carrots, soy sauce', 'No meat!')
]
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