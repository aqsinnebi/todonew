from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index,name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('search/', views.search, name='search'),
    path('update/<int:id>', views.update, name='update'),
    path('edit/<int:id>', views.edit, name='edit')
    
    
    
    ]