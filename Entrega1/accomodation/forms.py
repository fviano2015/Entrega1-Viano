from django import forms

class RoomForm(forms.Form):
    name = forms.CharField(max_length =100)
    price_day = forms.FloatField()
    available = forms.BooleanField(required = False)
    time = forms.FloatField()
    space = forms.FloatField()