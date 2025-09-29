from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class CarRegister(models.Model):
    full_name = models.CharField(max_length=100, default="Sample Name")
    email = models.EmailField(unique=True, default="sample@gmail.com")
    car_pic = models.ImageField(upload_to="images/")  # to add images to form
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.year})"


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class LuxuryCar(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    features = models.TextField()

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.year})"


# ✅ Signup/Profile Model
class Signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django user
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Rental(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    duration = models.PositiveIntegerField(help_text="Duration in days")  # Added rental duration field
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Rental by {self.full_name} for {self.duration} days"

class InsuranceQuote(models.Model):
    PLAN_CHOICES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    car_model = models.CharField(max_length=150)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    message = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.plan.capitalize()} Plan"
