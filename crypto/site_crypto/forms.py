from django import forms
from .models import Exchange, Assets, Deals
class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange
        fields = ['name', 'location', 'trade_volume']
        #fields = '__all__'
    
class AssetsForm(forms.ModelForm):
    class Meta:
        model = Assets
        fields = ['name', 'type', 'price']

class DealsForm(forms.ModelForm):
    class Meta:
        model = Deals
        #fields = ['asset', 'buying_ID', 'selling_ID', 'buying', 'selling', 'profit', 'time']
        # можно не перечислять все поля при создании формы указав просто __all__
        fields = '__all__'
