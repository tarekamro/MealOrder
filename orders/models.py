from django.db import models
from django.db.models import *
from meals.models import Meal
from django import forms

# Create your models here.


class Order(models.Model):
    PRODUCT_QUANTITY_CHOICES = tuple([(str(i), str(i)) for i in range(1, 10)])

    quantity = models.CharField(max_length=2, choices=PRODUCT_QUANTITY_CHOICES)
    order_no = models.IntegerField(primary_key=True,)
    # meal = models.ForeignKey(Meal, on_delete=DO_NOTHING, blank=True, null=True)
    meal = models.ForeignKey(Meal, on_delete=DO_NOTHING)
    ordered_at = models.DateTimeField(auto_now_add=True)
    requester = models.CharField(max_length=50)
    objects = models.Manager()

    def __str__(self):
        return '{}, Quantity: {}, Requester: {}'.format(self.meal, self.quantity, self.requester)


class OrderForm(forms.ModelForm):
    PRODUCT_QUANTITY_CHOICES = tuple([(str(i), str(i)) for i in range(1, 10)])
    quantity = forms.ChoiceField(choices=PRODUCT_QUANTITY_CHOICES)
    requester = models.CharField(max_length=50)

    class Meta:
        model = Order
        fields = ['quantity', 'requester']





