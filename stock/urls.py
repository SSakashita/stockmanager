from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('items/new/', views.items_new, name='items_new'),
    path('list', views.item_list, name='item_list'),
    path('setting', views.stock_setting, name='stock_setting' ),
]