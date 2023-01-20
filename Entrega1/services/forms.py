from django import forms

class TransportForm(forms.Form):
    type = forms.CharField(max_length = 100)
    time = forms.FloatField()
    place = forms.CharField(max_length=200)
    price = forms.FloatField()


class ActivityForm(forms.Form):
    name = forms.CharField(max_length = 50)
    time = forms.FloatField()
    price = forms.FloatField()
