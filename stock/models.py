from django.conf import settings
from django.db import models
from django import forms
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=20)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField('品名', max_length=20)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField('数量', default=1)
    price = models.PositiveIntegerField('価格', default=0)
    bought_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name

