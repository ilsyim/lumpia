from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('lumpias/', views.lumpias_index, name='lumpias_index'),
  path('lumpias/<int:lumpia_id>/', views.lumpias_detail, name='lumpias_detail'),
  path('lumpias/create/', views.LumpiaCreate.as_view(), name='lumpias_create'),
  path('lumpias/<int:pk>/update/', views.LumpiaUpdate.as_view(), name='lumpias_update'),
  path('lumpias/<int:pk>/delete/', views.LumpiaDelete.as_view(), name='lumpias_delete'),
  path('desserts/create/', views.DessertCreate.as_view(), name='desserts_create'),
  path('desserts/<int:pk>/', views.DessertDetail.as_view(), name='desserts_detail'),
  path('desserts/', views.DessertList.as_view(), name='desserts_index'),
]