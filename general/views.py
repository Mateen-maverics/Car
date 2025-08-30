from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from general.models import CarRegister, Contact
from .forms import SignUpForm


# Car purchase - login required
@login_required
def buy_car(request, car_id):
    try:
        car = CarRegister.objects.get(id=car_id)
    except CarRegister.DoesNotExist:
        return redirect("carlist")  # Redirect to car list if car not found
    return render(request, "buy_car.html", {"car": car})


# Signup page
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log user in
            return redirect("home")  # redirect to homepage
    else:
        form = SignUpForm()
    return render(request, "general/signup.html", {"form": form})


# Static pages
class HomePageView(TemplateView):
    template_name = 'general/index.html'


class LuxuryPageView(TemplateView):
    template_name = 'general/luxury.html'


class AboutPageView(TemplateView):
    template_name = 'general/about.html'


# Car Registration Page
class RegisterPageView(CreateView):
    template_name = 'general/carregister.html'
    model = CarRegister
    fields = '__all__'
    success_url = reverse_lazy('carlist')


# Contact Page
class ContactPageView(CreateView):
    template_name = 'general/contact.html'
    model = Contact
    fields = ['name', 'email', 'message']
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        response = super().form_valid(form)
        self.request.session['form_success'] = True
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.get('form_success'):
            context['success'] = True
            del self.request.session['form_success']
        return context


# Car List Page
class CarListView(ListView):
    model = CarRegister
    template_name = "general/carlist.html"
    context_object_name = "carregister_list"


# Contact Messages List
class ContactFormResultView(ListView):
    template_name = 'general/view_contact.html'
    model = Contact


# Car Details
class CarDetailView(DetailView):
    template_name = 'general/cardetail.html'
    model = CarRegister


# Contact Details
class ContactDetailView(DetailView):
    template_name = 'general/details.html'
    model = Contact


# Services Page
class ServicePageView(TemplateView):
    template_name = 'general/service.html'
