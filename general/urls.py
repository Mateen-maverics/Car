from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('carlist/', CarListView.as_view(), name='carlist'),
    path('cardetails/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('view_contact/', ContactFormResultView.as_view(), name='view_contact'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('carregister/', RegisterPageView.as_view(), name='car_register'),
    path('services/', ServicePageView.as_view(), name='services'),
    path('luxury/', LuxuryPageView.as_view(), name='luxury'),
    path('buy/<int:car_id>/', buy_car, name='buy_car'),  # Buying a car

    # 🔑 Auth
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="general/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="home"), name='logout'),
]
