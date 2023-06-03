from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Inventory
    path('warehouse/', views.warehouse, name='warehouse'),
    path('mainstore/', views.mainstore, name='mainstore'),
    path('branch/', views.branch, name='branch'),
    path('purchase_return/', views.purchase_return, name='purchase_return'),
    path('products_entry/', views.products_entry, name='products_entry'),

    # Transactions
    path('sales/', views.sales, name='sales'),
    
    
   
  
    



]