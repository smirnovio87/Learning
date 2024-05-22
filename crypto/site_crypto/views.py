from rest_framework import generics
from .models import Exchange
from .serializers import ExchangeSeriasizer

class ExcahgeList(generics.ListCreateAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSeriasizer
    
