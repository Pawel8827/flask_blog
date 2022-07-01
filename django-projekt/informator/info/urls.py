from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.test, name='index'),
   

    path('slider', Slider_List.as_view(), name='slider_list'),
    path('slider/<int:pk>/update', Slider_Update.as_view(extra_context={'title': 'Edycja'}), name='slider_update'),
    path('slider/<int:pk>/delete', Slider_Delete.as_view(), name='slider_delete'),
    path('slider/new',Slider_Create.as_view(extra_context={'title': 'Dodaj Slider'}), name='slider_create'),
    

    path('logo', Logo_List.as_view(extra_context={'title': 'Logo list'}), name='logo_list'),
    path('logo/<int:pk>', Logo_Detail.as_view(extra_context={'title': 'Nagłówek '}), name='logo_detail'),
    path('logo/new/', Logo_Create.as_view(extra_context={'title': 'Dodaj Slider'}), name='logo_create'),
    path('logo/<int:pk>/update', Logo_Update.as_view(extra_context={'title': 'Edycja Nagówka  '}), name='logo_update'),
    path('logo/<int:pk>/delete', Logo_Delete.as_view(), name='logo_delete'),
    
]