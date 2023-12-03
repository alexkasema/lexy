from django import forms
from django.forms.widgets import PasswordInput, EmailInput, Textarea

from . models import ProductReview

class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write a review'}))

    class Meta:
        model = ProductReview
        fields = ['review', 'rating']