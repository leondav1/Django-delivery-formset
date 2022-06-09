from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from app_delivery.forms import DeliveryForm, AddressFormSet
from app_delivery.models import File, Address, Delivery


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'delivery/delivery_list.html'
    context_object_name = 'deliveries'


class DeliveryCreate(View):
    def get(self, request):
        form = DeliveryForm()
        formset = AddressFormSet()
        return render(request, 'delivery/delivery_create.html', context={'form': form, 'formset': formset})

    def post(self, request):
        bound_form = DeliveryForm(request.POST, request.FILES)
        bound_form_set = AddressFormSet(request.POST)

        if bound_form.is_valid() and bound_form_set.is_valid():
            delivery = bound_form.save()
            for addr in bound_form_set.cleaned_data:
                if addr:
                    Address(addr=addr['addr'], delivery=delivery).save()
            file = request.FILES.get('file_field')
            if file:
                File(name=file.name, file=file, delivery=delivery).save()
            return redirect('delivery_list_url')
        return render(request, 'delivery/delivery_create.html', context={'form': bound_form, 'formset': bound_form_set})
