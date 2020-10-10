from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django import forms
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from pyzbar.pyzbar import decode
from PIL import Image
from bs4 import BeautifulSoup
import requests
import re

from .models import Item, Category, Photo
from .forms import AddCategoryForm, AddItemForm, PhotoForm


@login_required
def index(request):
  categorys = Category.objects.filter(author=request.user)
  return render(request, 'stock/index.html', {'categorys':categorys})


@login_required
def items_new(request):
  item_name_from_code = ''
  if request.method == 'POST':
    if 'item_form' in request.POST:
      item_form = AddItemForm(request.POST)
      if item_form.is_valid():
        item = item_form.save(commit=False)
        item.author = request.user
        item = item_form.save()
        return redirect('item_list')
    elif 'photo_form' in request.POST:
      photo_form = PhotoForm(request.POST, request.FILES)
      if not photo_form.is_valid():
        raise ValueError('invalid form')
      photo = Photo()
      photo.image = photo_form.cleaned_data['image']
      data = decode(Image.open(photo.image))
      number = data[0][0].decode('utf-8', 'ignore')

      keyword =  str(number)
      search_url = "https://search.rakuten.co.jp/search/mall/"
      item_name_from_code = get_html(search_url, keyword)

      default_data = {'name': item_name_from_code}
      item_form = AddItemForm(initial=default_data)
  else:
    item_form = AddItemForm()
    photo_form = PhotoForm()

  return render(request, 'stock/items_new.html', {'item_form': item_form, 'photo_form': photo_form})


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

@login_required
def category_remove(request, pk):
  category = get_object_or_404(Category, pk=pk)
  category.delete()
  return redirect('setting_category')


@login_required
def barcode_input(request):
  if request.method == 'GET':
    return render(request, 'stock/barcode_input.html', {'form': PhotoForm(),})
  elif request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    if not form.is_valid():
      raise ValueError('invalid form')
    photo = Photo()
    photo.image = form.cleaned_data['image']
    data = decode(Image.open(photo.image))
    number = data[0][0].decode('utf-8', 'ignore')

    keyword =  str(number)
    search_url = "https://search.rakuten.co.jp/search/mall/"
    item_name = get_html(search_url, keyword)
    return render_to_response('stock/barcode_input.html', {'number': number, 'item_name': item_name})

@login_required
def search_code(request):
  keyword = '4902102112109'
  search_url = "https://search.rakuten.co.jp/search/mall/"
  text = get_html(search_url, keyword)
  return render(request, 'stock/search_code.html',{'text': text})


def get_html(url, keyword):
  search_url = url + keyword + ' 商品名'
  response = requests.get(search_url)
  html = response.text
  #htmlパーサー
  soup = BeautifulSoup(html,'html.parser')
  items = soup.select(' .searchresultitem')
  item_name_list = []
  item_name_contents_list = []
  for item in items:
    item_name = item.select_one(' .title')
    item_name_contents_list += re.split('[ 】]', item_name.text)
  name_start_not = [s for s in item_name_contents_list if not s.startswith('【')]
  if not name_start_not:
    text = 'Not Found'
  else:
    text = name_start_not[0]
  return text