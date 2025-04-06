from cars.models import Car, Brand
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView ,CreateView, DetailView, UpdateView,DeleteView

# Create your views here.

class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search=self.request.GET.get('search')
        if search:
            cars=cars.filter(model__icontains=search)
        return cars

@method_decorator(login_required(login_url='login'),name='dispatch')   
class NewCarCreateView(CreateView):
    model = Car
    template_name = 'new_car.html'
    form_class = CarModelForm
    success_url = '/cars/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()  # Envia todas as marcas para o template
        return context


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['cars_list'] = Car.objects.all()
        return context

@method_decorator(login_required(login_url='login'),name='dispatch')   
class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_update.html'
    form_class = CarModelForm

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk':self.object.pk})
                 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()  # Envia todas as marcas para o template
        return context
    
@method_decorator(login_required(login_url='login'),name='dispatch')      
class CarDeleteView(DeleteView):
    model=Car
    template_name='car_delete.html'
    success_url='/cars/'