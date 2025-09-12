from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    email=forms.EmailField(label="Enter your email", max_length=100)
    name=forms.CharField(label="Enter your name", max_length=100)
    feedback=forms.CharField(label="Your Feedback", widget=forms.Textarea)
    class Meta:
        model = Feedback
        fields=['email','name','feedback']
