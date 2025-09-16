from django.urls import path
from .views import (
    HomePageView, AboutPageView, ContactPageView, CarListView, CarDetailView,
    ContactFormResultView, ContactDetailView, RegisterPageView, ServicePageView,
    LuxuryPageView, AdminPageView, buy_car, SignupView, CustomLoginView, CustomLogoutView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('carlist/', CarListView.as_view(), name='carlist'),
    path('cardetails/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('view_contact/', ContactFormResultView.as_view(), name='view_contact'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('carregister/', RegisterPageView.as_view(), name='car_register'),
    path("services/", ServicePageView.as_view(), name="services"),
    path('luxury/', LuxuryPageView.as_view(), name='luxury'),
    path('adminsite/', AdminPageView.as_view(), name='adminsite'),    
    path('buy/<int:car_id>/', buy_car, name='buy_car'),

    # 🔑 Auth
    path('signup/', SignupView.as_view(), name='signup'),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]

