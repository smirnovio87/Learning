
from rest_framework import serializers
from .models import Exchange


class ExchangeSeriasizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exchange
        fields = ["uuid", "name", "location", "trade_volume"]
