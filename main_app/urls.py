from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('lumpias/', views.lumpias_index, name='lumpias_index'),
]