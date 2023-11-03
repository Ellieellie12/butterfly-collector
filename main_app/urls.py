from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('butterflies/', views.butterfly_index, name='butterfly-index'),
  path('butterflies/<int:butterfly_id>/', views.butterfly_detail, name='butterfly-detail'),
  path('butterflies/create/', views.ButterflyCreate.as_view(), name='butterfly-create'),
  path('butterflies/<int:pk>/update/', views.ButterflyUpdate.as_view(), name='butterfly-update'),
  path('butterflies/<int:pk>/delete/', views.ButterflyDelete.as_view(), name='butterfly-delete'),
]