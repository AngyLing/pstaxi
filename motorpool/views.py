from django.shortcuts import render
from django.views.generic import DetailView, ListView
from motorpool.models import Brand


class BrandListView(ListView):
    model = Brand
    template_name = 'motorpool/brand_list.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand_number'] = Brand.objects.count()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-pk')


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'motorpool/brand_detail.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        default_object = super().get_object(queryset)
        return default_object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = self.object.cars.all()
        return context

    def get_template_names(self):
        default_template_names = super().get_template_names()
        return default_template_names

