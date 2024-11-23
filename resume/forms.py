from django import forms
from .models import Resume
from django.core.exceptions import ValidationError
import re

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'First_Name', 'Last_Name', 'email', 'phone', 'address', 'education',
            'experience', 'skills', 'summary', 'profile_image', 'date_of_birth',
            'nationality', 'city', 'postal_code', 'country', 'web', 'about_you',
        ]
        widgets = {
            'First_Name': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'First Name'}),
            'Last_Name': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'custom-input', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'custom-input', 'type': 'tel', 'placeholder': 'Phone'}),
            'address': forms.Textarea(attrs={'class': 'custom-textarea', 'placeholder': 'Address'}),
            'education': forms.Textarea(attrs={'class': 'custom-textarea', 'placeholder': 'Education'}),
            'experience': forms.Textarea(attrs={'class': 'custom-textarea', 'placeholder': 'Experience'}),
            'skills': forms.Textarea(attrs={'class': 'custom-textarea', 'placeholder': 'Skills'}),
            'summary': forms.Textarea(attrs={'class': 'custom-textarea', 'placeholder': 'Summary'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'custom-input', 'type': 'date'}),
            'nationality': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Nationality'}),
            'city': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'City'}),
            'postal_code': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Postal'}),
            'country': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Country'}),
            'web': forms.URLInput(attrs={'class': 'custom-input', 'placeholder': 'Web'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\+?1?\d{9,15}$', phone):
            raise ValidationError("Phone number must be in the format: '+999999999'. Up to 15 digits allowed.")
        return phone
