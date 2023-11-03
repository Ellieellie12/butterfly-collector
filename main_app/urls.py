from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('butterflies/', views.butterfly_index, name='butterfly-index'),
  path('butterflies/<int:butterfly_id>/', views.butterfly_detail, name='butterfly-detail'),
  path('butterflies/create/', views.ButterflyCreate.as_view(), name='butterfly-create')
]