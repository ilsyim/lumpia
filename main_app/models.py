from turtle import filling
from django.db import models

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

