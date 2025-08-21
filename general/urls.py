from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('carlist/', CarListView.as_view(), name='carlist'),
    path('cardetails/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('view_contact/', ContactFormResultView.as_view(), name='view_contact'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('carregister/', RegisterPageView.as_view(), name='car_register'),
]