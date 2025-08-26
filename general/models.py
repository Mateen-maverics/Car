from django.db import models

# Create your models here.
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
    car_pic = models.ImageField(upload_to="images/") #to add images to form
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.year})"