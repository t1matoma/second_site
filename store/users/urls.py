from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='log'),
    path('register/', views.register, name='reg'),
    path('profile/', views.profile, name='prof'),
    path('logout/', views.logout, name='logout'),


]
