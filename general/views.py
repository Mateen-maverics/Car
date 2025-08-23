from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from general.models import *
#
#  Create your views here.

class HomePageView(TemplateView):
    template_name = 'general/index.html'

    
class AboutPageView(TemplateView):
    template_name = 'general/about.html'
    
class RegisterPageView(CreateView):
    template_name = 'general/carregister.html'
    model = CarRegister
    fields = '__all__'
    success_url = '/carlist/'  # Redirect to the car list page after successful registration
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Save uploaded file and form data
        return super().form_valid(form)

    


class ContactPageView(CreateView):
    template_name = 'general/contact.html'
    model = Contact
    fields = ['name', 'email', 'message']
    success_url = '/contact/'  # Redirect to the view contact page after successful submission
    def form_valid(self, form):
        # Save the contact form data
        response = super().form_valid(form)
        self.request.session['form_success'] = True     
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.get('form_success'):
            context['success'] = True
            del self.request.session['form_success']
        return context
    
class CarListView(ListView):
    model = CarRegister
    template_name = "general/carlist.html"

class ContactFormResultView(ListView):
    template_name = 'Car/view_contact.html'
    model = Contact

class CarDetailView(DetailView):
    template_name = 'general/cardetail.html'
    model = CarRegister

class ContactDetailView(DetailView):
    template_name = 'general/details.html'
    model = Contact

class ServicePageView(TemplateView):
    template_name = 'general/service.html'
