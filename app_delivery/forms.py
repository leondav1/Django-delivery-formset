from django import forms
from django.forms import inlineformset_factory

from app_delivery.models import Delivery, Address


class DeliveryForm(forms.ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(), label='Загрузить файл', required=False)

    class Meta:
        model = Delivery
        fields = ['title', 'product_type', 'delivery_date', 'file_field']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'product_type': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select a date',
                'type': 'date'
            }),
        }


AddressFormSet = inlineformset_factory(Delivery, Address, fields=['addr'], can_delete_extra=False, extra=5, widgets={
    'addr': forms.TextInput(attrs={'class': 'form-control'}),
})
