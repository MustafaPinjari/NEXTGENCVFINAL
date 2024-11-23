from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_resume, name="create_resume"),
    path("download/<str:format>/", views.download_resume, name="download_resume"),
    path("generate_pdf/", views.generate_pdf, name="generate_pdf"),
]
