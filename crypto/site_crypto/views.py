from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Exchange, Assets, Deals
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AssetsForm, ExchangeForm, DealsForm
import json

# Отображаем Index
def index(request):
    return TemplateResponse(request, 'index.html')
def subscribe(request):
    return TemplateResponse(request, 'site_crypto/subscribe.html')

# Отображаем forms
def forms (request):
    # Если это POST запрос нужно обработать данные, полученные из формы
    if request.method == 'POST':
        # Создаем экземпляр формы и заполняем ее
        form = ExchangeForm(request.POST)
        # Если форма верно заполнена сохраняем
        print(dir(form))
        print("////")
        print(form)
        if form.is_valid():
            form.save()
            # Перенаправляем на новый URL (Тут вопрос)
            return HttpResponseRedirect(redirect_to="/")
    #Создаем пустую форму    
    form=ExchangeForm()
    context={'form':form}
    return render(request, 'site_crypto/forms.html', context)
        

def get_exchange(request):
    table=Exchange.objects.all()
    name=Exchange.objects.get(name="ByBit")
    out={}
    namenew = name.__dict__
    # print(type(namenew))
    for i in namenew.items():
        out[i[0]] = str(i[1])
    print(out)
    return JsonResponse(out)
def get_assets(request):
    asset=Assets.objects.all()
    context={"asset": asset}
    return render(request, 'site_crypto/asset.html', context)

def price(request):
    with open('btc_usdt_courses_12.json') as file:
         data=json.load(file)
    context = {'context': data}

    return render(request, 'site_crypto/price.html', context)

def profile(request):
    return render(request, 'site_crypto/profile.html')




