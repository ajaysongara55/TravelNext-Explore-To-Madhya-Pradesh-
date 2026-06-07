from django.urls import path
from . import views



urlpatterns = [
    path("",views.index),   
    path("login",views.login),
    path("traveler",views.traveler),
    path("registration",views.registration),
    path("contact",views.contact),
    path("about",views.about),
    path("home",views.home),
    path("locations",views.locations),
    path("Ujjain",views.Ujjain),
    path("Indore",views.Indore),
    path("Bhopal",views.Bhopal),
    path("Pachmarhi",views.Pachmarhi),
    path("Omkareshwar",views.Omkareshwar),
    path("Jabalpur",views.Jabalpur),
    path("Vidisha",views.Vidisha),
    path("Khajuraho",views.Khajuraho),
    path("Kuno",views.Kuno),
    path("Rewa",views.Rewa),
    path("Shahdol",views.Shahdol),
    path("Mandsaur",views.Mandsaur),
    path("Gwalior",views.Gwalior),
    path("hotel",views.hotel)
]