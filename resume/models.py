# resume/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50, default='Unknown')  # Added default value
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    summary = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
    # New fields added
    date_of_birth = models.DateField(null=True, blank=True)  # Date of Birth
    nationality = models.CharField(max_length=50, null=True, blank=True)  # Nationality
    city = models.CharField(max_length=50, null=True, blank=True)  # City
    postal_code = models.CharField(max_length=20, null=True, blank=True)  # Postal Code
    country = models.CharField(max_length=50, null=True, blank=True)  # Country
    web = models.URLField(null=True, blank=True)  # Web Address
    about_you = models.TextField(null=True, blank=True)  # New field for user description

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"
