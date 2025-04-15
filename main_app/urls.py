from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name='about'), 
     path('cats/', views.cats_index, name='cats_index'),  # Updated name
     path('cats/<int:cat_id>/', views.cat_detail, name='cat_detail'),  # Updated name
     path('cats/create/', views.CatCreate.as_view(), name='cat-create'),  # Updated name
     path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),  # Updated name
     path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),  # Updated name
]

