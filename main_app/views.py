from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Butterfly


class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def butterfly_index(request):
  butterflies = Butterfly.objects.filter(user=request.user)
  return render(request, 'butterflies/index.html', { 'butterflies': butterflies })

@login_required
def butterfly_detail(request, butterfly_id):
  butterfly = Butterfly.objects.get(id=butterfly_id)
  return render(request, 'butterflies/detail.html', { 'butterfly': butterfly })

class ButterflyCreate(LoginRequiredMixin, CreateView):
  model = Butterfly
  fields = ['name', 'species', 'description', 'age']
  # success_url = '/butterflies/'
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class ButterflyUpdate(LoginRequiredMixin, UpdateView):
  model = Butterfly
  fields =['species', 'description', 'age']

class ButterflyDelete(LoginRequiredMixin, DeleteView):
  model = Butterfly
  success_url = '/butterflies/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('butterfly-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)