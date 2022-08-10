from distutils.text_file import TextFile
from django.db import models
from django.urls import reverse

# Create your models here.
PROTEINS = (
  ('B', 'Beef'),
  ('C', 'Chicken'),
  ('F', 'Fish'),
  ('P', 'Pork'),
  ('T', 'Turon'),
  ('V', 'Vegetarian')
)

class Lumpia(models.Model):
  protein = models.CharField(
    max_length=1,
    choices=PROTEINS,
    default=PROTEINS[0][0]
  )
  fillings = models.TextField(max_length=250)
  review = models.TextField(max_length=250)

  def get_absolute_url(self):
    return reverse('lumpias_detail', kwargs={'lumpia_id': self.id})
  
class Dessert(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=30)
  description = models.TextField(max_length=150)
  ingredients = models.TextField(max_length=300)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse('desserts_detail', kwargs={'pk': self.id})
  