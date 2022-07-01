
from django.shortcuts import render , get_object_or_404
from .forms import NaglowekForm, SliderForm
from .models import Naglowek, Slider
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from datetime import datetime
from django.urls import reverse
from django.db.models import Q
    
class Logo_List(ListView):
    model = Naglowek
    template_name = 'logo_list.html'
    context_object_name = 'nag'

    
    
class Logo_Detail(DetailView):
    model = Naglowek
    template_name = 'logo_detail.html'
    context_object_name = 'i'
    
class Logo_Create(CreateView):
    model = Naglowek
    form_class = NaglowekForm
    template_name = 'new.html'

    def form_valid(self, form):
        #print(form.cleaned_data)
        return super().form_valid(form)

class Logo_Update(UpdateView):
    model = Naglowek
    form_class = NaglowekForm
    template_name = 'new.html'

    def form_valid(self, form):
        #print(form.cleaned_data)
        return super().form_valid(form)
    
class Logo_Delete(DeleteView):
    template_name = 'logo_delete.html'

    def get_object(self):
        id_ =self.kwargs.get('pk')
        return get_object_or_404(Naglowek, id=id_)

    def get_success_url(self):
        return reverse('logo_list')

class Slider_List(ListView):
    model=Slider
    template_name = 'slider_list.html'
    context_object_name = 'slid' 
   
    #queryset = Slider.objects.filter(Q(Data_wygasniecia__gte=today)|Q(Data_wygasniecia=None))

    
class Slider_Update(UpdateView):
    model=Slider
    form_class= SliderForm
    template_name = 'new.html'
    succes_url = '/slider'

    
class Slider_Create(CreateView):
    model = Slider
    form_class = SliderForm
    template_name = 'new.html'
    succes_url = '/slider'
    

class Slider_Delete(DeleteView):
    template_name = 'slider_delete.html'

    def get_object(self):
        id_ =self.kwargs.get('pk')
        return get_object_or_404(Slider, id=id_)

    def get_success_url(self):
        return reverse('slider_list')
    


def test(request):
    naglowek = Naglowek.objects.filter(unike=True)
    today = datetime.today()
    slider = Slider.objects.filter(Q(Data_wygasniecia__gte=today)|Q(Data_wygasniecia=None)).order_by('-Data_Utworzenia')
    return render(request, 'index.html', {'nag':naglowek , 'slid':slider})

