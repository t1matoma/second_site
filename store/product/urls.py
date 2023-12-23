from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='prod'),
    path('category/<int:category_id>/', views.products, name='category'),
    path('pages/<int:page_number>/', views.products, name='pages'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),

]
