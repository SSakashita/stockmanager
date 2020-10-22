from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('items/new/', views.items_new, name='items_new'),
    path('list/', views.item_list, name='item_list'),
    path('item/<int:pk>/detail/', views.item_detail, name='item_detail'),
    path('item/<int:pk>/edit/', views.item_edit, name='item_edit'),
    path('item/<int:pk>/remove', views.item_remove, name='item_remove'),
    path('item/<int:pk>/remove/confirm', views.item_remove_confirm, name='item_remove_confirm'),
    path('setting', views.stock_setting, name='stock_setting' ),
    path('setting/category', views.setting_category, name='setting_category'),
    path('setting/category/new', views.category_new, name='category_new'),
    path('setting/category/<pk>/remove/', views.category_remove, name='category_remove'),
    path('items/new/barcodeinput', views.barcode_input, name='barcode_input'),
    path('items/searchcode', views.search_code, name='search_code'),
]