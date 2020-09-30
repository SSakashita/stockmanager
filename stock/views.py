from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# from .forms import AddItemsFormSet
from .models import Item


@login_required
def index(request):
  return render(request, 'stock/index.html')


# @login_required
# def items_new(request):
#   formset = AddItemsFormSet

#   return render_to_response('stock/items_new.html', {'formset': formset})


@login_required
def items_new(request):
  AddItemsFormSet = forms.modelformset_factory(
    model=Item,
    fields={'name', 'category', 'quantity', 'price'},
    extra=2
    )
  if request.method == 'POST':
    formset = AddItemsFormSet(request.POST, queryset=Item.objects.none())
    if formset.is_valid():
      formset.save()
      data = [x.test for x in Item.objects.all()]
      return HttpResponse(repr(data))
  else:
    formset = AddItemsFormSet(queryset=Item.objects.none())
  return render(request, 'stock/items_new.html', {'formset': formset})


@login_required
def item_list(request):
  items = Item.objects.order_by('bought_date')
  return render(request, 'stock/item_list.html',{'items': items})


@login_required
def stock_setting(request):
  return render(request, 'stock/setting.html')