from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Exchange, Assets, Deals
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import AssetsForm, ExchangeForm, DealsForm

def index(request):
    return TemplateResponse(request, 'index.html')
def forms (request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect
    form=ExchangeForm()
    context={'form':form}
    return render(request, 'site_crypto/forms.html', context)
        

def get_exchange(request):
    table=Exchange.objects.in_bulk()
    # return table
    return HttpResponse(table)
    
# Create your views here.
