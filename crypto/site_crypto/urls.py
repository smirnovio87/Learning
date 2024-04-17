from django.urls import path
from site_crypto import views

urlpatterns = [
   path("exch/", views.get_exchange)
]

