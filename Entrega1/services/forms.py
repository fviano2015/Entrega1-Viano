from django import forms

class TransportForm(forms.Form):
    type = forms.CharField(max_length = 100)
    time = forms.FloatField()
    where = forms.CharField(max_length=200)
    price = forms.FloatField()
