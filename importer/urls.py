from django.urls import path
from . import views

urlpatterns = [
    path('execute/', views.call_importer, name="importer"),
]
