from django import forms

from .models import Item, Category

class AddItemForm(forms.ModelForm):

    class Meta:
      model =Item
      fields = ('name', 'category', 'quantity', 'price')

# AddItemsFormset = forms.inlineformset_factory(Item, AddItemForm, extra=1, max_num=30)


class AddCategoryForm(forms.ModelForm):

  class Meta:
    model = Category
    fields = {'name',}