from .views import ContactView
from . import views
from django.urls import path 

urlpatterns = [
    path("", ContactView.as_view, name="contact"),
    
   
]