from django.db import models
from django import forms

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    email_id=models.EmailField(max_length=100)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to="testimonials/")
    rating = models.IntegerField(max_length=1)

    def __str__(self):
        return self.testimonial
    

class Feedback(models.Model):
    email=forms.EmailField(label="Enter your email", max_length=100)
    name=forms.CharField(label="Enter your name", max_length=100)
    feedback=forms.CharField(label="Your Feedback", widget=forms.Textarea)

    def __str__(self):
        return self.name
