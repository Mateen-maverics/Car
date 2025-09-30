from django.contrib import admin
from general.models import Contact, CarRegister, Rental, InsuranceQuote

# Register your models here.
admin.site.register(Contact)
admin.site.register(CarRegister)
admin.site.register(Rental)
admin.site.register(InsuranceQuote)