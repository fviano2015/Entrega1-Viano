from django.shortcuts import render


from accomodation.models import Rooms
from accomodation.forms import  RoomForm 



def create_room(request):
    if request.method == 'GET':
        context = {'form': RoomForm()}
        return render(request, 'accomodation/create_room.html', context = context)
    elif request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            Rooms.objects.create(
                name = form.cleaned_data['name'],
                price_day = form.cleaned_data['price_day'],
                available = form.cleaned_data['available'],
                time = form.cleaned_data['time'],
                space = form.cleaned_data['space'],
            )
            context = {
                'message' : "Cuarto creado exitosamente"
            } 
            return render(request, 'accomodation/create_room.html', context = context)
        else:
            context = {
                'form errors': form.errors,
                'form' : RoomForm()
                }
            return render(request, 'accomodation/create_room.html', context = context)



def list_rooms(request):
    if 'search' in request.GET:
        search = request.GET['search']
        rooms = Rooms.objects.filter(name__contains = search)
    else:
        rooms = Rooms.objects.all()
    context = {
        'rooms' : rooms
        }
    return render(request, 'accomodation/list_rooms.html', context = context)