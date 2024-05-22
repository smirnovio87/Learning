from django.urls import path
# from site_crypto import views
from .views import ExcahgeList

urlpatterns = [
   # path("", views.index, name="index"),
   # path("exch/", views.get_exchange, name="exch"),
   # path("forms/", views.forms, name="forms"),
   # path("asset/", views.get_assets, name="asset"),
   # path("subscribe/", views.subscribe, name="subscribe"),
   # path("price/", views.price, name="price")
   path('exchange/', ExcahgeList.as_view(), name="ExchangeList")
   
]

