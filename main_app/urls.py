from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('lumpias/', views.lumpias_index, name='lumpias_index'),
  path('lumpias/<int:lumpia_id>/', views.lumpias_detail, name='lumpias_detail'),
  path('lumpias/create/', views.LumpiaCreate.as_view(), name='lumpias_create'),
]