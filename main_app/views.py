from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Butterfly


class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def butterfly_index(request):
  butterflies = Butterfly.objects.all()
  return render(request, 'butterflies/index.html', { 'butterflies': butterflies })

def butterfly_detail(request, butterfly_id):
  butterfly = Butterfly.objects.get(id=butterfly_id)
  return render(request, 'butterflies/detail.html', { 'butterfly': butterfly })

class ButterflyCreate(CreateView):
  model = Butterfly
  fields = ['name', 'species', 'description', 'age']
  # success_url = '/butterflies/'
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class ButterflyUpdate(UpdateView):
  model = Butterfly
  fields =['species', 'description', 'age']

class ButterflyDelete(DeleteView):
  model = Butterfly
  success_url = '/butterflies/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)