from django.shortcuts import render

from motorpool.models import Brand
from utils.text import plural_form


def brand_list(request):
    template_name = 'motorpool/brand_list.html'
    brand_objects = Brand.objects.all()
    brand_number = brand_objects.count()
    context = {
        'brand_objects': brand_objects,
        'brand_number': brand_number,
        'brand_plural_form': plural_form(brand_number,
                                         'топовый бренд автомобиля',
                                         'топовых бренда автомобилей',
                                         'топовых брендов автомобилей',),
    }
    return render(request, template_name, context)

