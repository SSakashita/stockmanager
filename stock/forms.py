from django import forms

from .models import Item

class AddItemForm(forms.ModelForm):

    class Meta:
      model =Item
      fields = ('name', 'category', 'quantity', 'price')

#AddItemsFormset = forms.inlineformset_factory(Item, AddItemForm, extra=0)
