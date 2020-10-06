from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# from .forms import AddItemsFormSet
from .models import Item, Category, Photo
from .forms import AddCategoryForm, AddItemForm, PhotoForm


@login_required
def index(request):
  categorys = Category.objects.filter(author=request.user)
  return render(request, 'stock/index.html', {'categorys':categorys})


@login_required
def items_new(request):
  if request.method == 'GET':
    return render(request, 'stock/items_new.html', {'form': PhotoForm(),})
  elif request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    if not form.is_valid():
      raise ValueError('invalid form')
    photo = Photo()
    photo.image = form.cleaned_data['image']
    photo.save()
    return redirect('item_list')




@login_required
def item_list(request):
  items = Item.objects.filter(author=request.user)
  return render(request, 'stock/item_list.html',{'items': items})


@login_required
def stock_setting(request):
  return render(request, 'stock/setting.html')


@login_required
def setting_category(request):
  categorys = Category.objects.filter(author=request.user)
  return render(request, 'stock/setting_category.html',{'categorys': categorys})


@login_required
def category_new(request):
  if request.method == 'POST':
    form = AddCategoryForm(request.POST)
    if form.is_valid():
      category = form.save(commit=False)
      category.author = request.user
      category = form.save()
      return redirect('setting_category')
  else:
      form = AddCategoryForm()
  return render(request, 'stock/category_new.html', {'form': form})


def category_remove(request, pk):
  category = get_object_or_404(Category, pk=pk)
  category.delete()
  return redirect('setting_category')

