from django.urls import path
from site_crypto import views

urlpatterns = [
   path("", views.index),
   path("exch/", views.get_exchange, name="exch"),
   path("forms/", views.forms, name="forms")
]
