from django.shortcuts import render
from services.models import Transport

from services.forms import  TransportForm 


def create_transport(request):
    if request.method == 'GET':
        context = {'form': TransportForm()}
        return render(request, 'services/create_transport.html', context = context)
    elif request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            Transport.objects.create(
                type = form.cleaned_data['type'],
                time = form.cleaned_data['time'],
                where = form.cleaned_data['where'],
                price = form.cleaned_data['price'],
            )
            context = {
                'message' : "Forma de transporte creada"
            } 
            return render(request, 'services/create_transport.html', context = context)
        else:
            context = {
                'form errors': form.errors,
                'form' : TransportForm()
                }
            return render(request, 'services/create_transport.html', context = context)
