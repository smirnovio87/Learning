from django.shortcuts import render
from site_crypto import models
from django.http import HttpResponse


def get_exchange(request):
    table=models.Exchange.objects.all()
    # return table
    return HttpResponse(table)
    
# Create your views here.
