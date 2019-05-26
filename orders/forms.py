from django import forms
from . import models

class OrderForm(forms.ModelForm):
    PRODUCT_QUANTITY_CHOICES = tuple([(str(i), str(i)) for i in range(1, 10)])
    quantity = forms.ChoiceField(choices=PRODUCT_QUANTITY_CHOICES)
    requester = models.CharField(max_length=50)

    class Meta:
        model = models.Order
        fields = ['quantity', 'requester']

