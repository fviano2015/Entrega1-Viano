from django.shortcuts import render
from services.models import Transport, Activities

from services.forms import  TransportForm, ActivityForm


def create_transport(request):
    if request.method == 'GET':
        context = {'form': TransportForm()}
        return render(request, 'services/create-transport.html', context = context)
    elif request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            Transport.objects.create(
                type = form.cleaned_data['type'],
                time = form.cleaned_data['time'],
                place = form.cleaned_data['place'],
                price = form.cleaned_data['price'],
            )
            context = {
                'message' : "Forma de transporte creada"
            } 
            return render(request, 'services/create-transport.html', context = context)
        else:
            context = {
                'form errors': form.errors,
                'form' : TransportForm()
                }
            return render(request, 'services/create-transport.html', context = context)


def list_transports(request):
    if 'search' in request.GET:
        search = request.GET['search']
        transport = Transport.objects.filter(name__contains = search)
    else:
        transport = Transport.objects.all()
    context = {
        'transports' : transport
        }
    return render(request, 'services/list-transport.html', context = context)



def services(request):
    return render(request, 'services/services.html', context = {})


def create_activity(request):
    if request.method == 'GET':
        context = {'form': ActivityForm()}
        return render(request, 'services/create-activity.html', context = context)
    elif request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            Activities.objects.create(
                name = form.cleaned_data['name'],
                time = form.cleaned_data['time'],
                price = form.cleaned_data['price'],
            )
            context = {
                'message' : "Actividad creada"
            } 
            return render(request, 'services/create-activity.html', context = context)
        else:
            context = {
                'form errors': form.errors,
                'form' : ActivityForm()
                }
            return render(request, 'services/create-activity.html', context = context)



def list_activities(request):
    if 'search' in request.GET:
        search = request.GET['search']
        transport = Activities.objects.filter(name__contains = search)
    else:
        activity = Activities.objects.all()
    context = {
        'activities' : activity
        }
    return render(request, 'services/list-activities.html', context = context)