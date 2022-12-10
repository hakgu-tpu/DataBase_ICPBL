from django.shortcuts import render
from .models import Car, Park
from common.models import User
# Create your views here.

def inquiry(request, id):
    owner = User.objects.get(user_id = id)
    objects_list = Car.objects.filter(owner = owner)
    context = {'inquiry_list': objects_list}
    return render(request, 'parking2.html', context)

def parking_map(request, building_num):
    objects_list = Park.objects.filter(location = building_num)
    context = {'inquiry_list': objects_list}
    return render(request, 'parking1.html', context)
