from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Lumpia, Dessert

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
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('lumpias_index')
    else:
      error_message = 'Invalid sign up -- please try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
