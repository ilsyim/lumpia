from django.shortcuts import render


class Lumpia:
  def __init__(self, protein, fillings, review):
    self.protein = protein
    self.filings = fillings 
    self.review = review
  
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
  return render(request, 'lumpias/index.html', {'lumpias': lumpias})