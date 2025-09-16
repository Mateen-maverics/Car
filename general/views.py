from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from general.models import CarRegister, Contact, signup
from .forms import SignUpForm, LoginForm


# ================== AUTH ================== #
class CustomLoginView(LoginView):
    template_name = 'general/login.html'
    authentication_form = LoginForm  # uses your custom LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class SignupView(CreateView):
    model = signup
    form_class = SignUpForm
    template_name = "general/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        # automatically log user in after signup
        login(self.request, self.object)
        return response


# ================== CAR PURCHASE ================== #
@login_required
def buy_car(request, car_id):
    try:
        car = CarRegister.objects.get(id=car_id)
    except CarRegister.DoesNotExist:
        return redirect("carlist")  # Redirect to car list if car not found
    return render(request, "buy_car.html", {"car": car})


# ================== STATIC PAGES ================== #
class HomePageView(TemplateView):
    template_name = 'general/index.html'


class LuxuryPageView(TemplateView):
    template_name = 'general/luxury.html'


class AdminPageView(TemplateView):
    template_name = 'general/admin.html'


class AboutPageView(TemplateView):
    template_name = 'general/about.html'


# ================== CAR REGISTRATION ================== #
class RegisterPageView(CreateView):
    template_name = 'general/carregister.html'
    model = CarRegister
    fields = '__all__'
    success_url = reverse_lazy('carlist')


# ================== CONTACT ================== #
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


# ================== CAR LIST & DETAILS ================== #
class CarListView(ListView):
    model = CarRegister
    template_name = "general/carlist.html"
    context_object_name = "carregister_list"


class CarDetailView(DetailView):
    template_name = 'general/cardetail.html'
    model = CarRegister


# ================== CONTACT LIST & DETAILS ================== #
class ContactFormResultView(ListView):
    template_name = 'general/view_contact.html'
    model = Contact


class ContactDetailView(DetailView):
    template_name = 'general/details.html'
    model = Contact


# ========
