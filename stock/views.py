from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#from .forms import AddItemForm, AddItemsFormSet
from .models import Item


@login_required
def index(request):
  return render(request, 'stock/index.html')


@login_required
def items_new(request):
  AddItemsFormSet = forms.modelformset_factory(
    model=Item,
    fields={'name', 'category', 'quantity', 'price'},
    extra=10
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