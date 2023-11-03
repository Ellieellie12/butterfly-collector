from django.shortcuts import render

class Butterfly: 
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

butterflies = [
  Butterfly('Lila', 'Monarch', 'Massive Wings', 3),
  Butterfly('Maggie', 'Monarch', 'small and orange', 2,)
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def butterfly_index(request):
  return render(request, 'butterflies/index.html', { 'butterflies': butterflies })