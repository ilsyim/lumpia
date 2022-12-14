from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('lumpias/', views.lumpias_index, name='lumpias_index'),
  path('lumpias/<int:lumpia_id>/', views.lumpias_detail, name='lumpias_detail'),
  path('lumpias/create/', views.LumpiaCreate.as_view(), name='lumpias_create'),
  path('lumpias/<int:pk>/update/', views.LumpiaUpdate.as_view(), name='lumpias_update'),
  path('lumpias/<int:pk>/delete/', views.LumpiaDelete.as_view(), name='lumpias_delete'),
  path('desserts/create/', views.DessertCreate.as_view(), name='desserts_create'),
  path('desserts/<int:pk>/', views.DessertDetail.as_view(), name='desserts_detail'),
  path('desserts/', views.DessertList.as_view(), name='desserts_index'),
    path('desserts/<int:pk>/update/', views.DessertUpdate.as_view(), name='desserts_update'),
  path('desserts/<int:pk>/delete/', views.DessertDelete.as_view(), name='desserts_delete'),
  path('lumpias/<int:lumpia_id>/assoc_dessert/<int:dessert_id>/', views.assoc_dessert, name='assoc_dessert'),
  path('accounts/signup', views.signup, name='signup')
]