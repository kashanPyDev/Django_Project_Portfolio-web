from portfolio_website import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='home'),
    path('saveFormData/', views.saveFormData, name='saveFormData'),
    
]