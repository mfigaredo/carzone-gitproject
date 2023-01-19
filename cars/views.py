from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Car

# Create your views here.
def cars(request):
  return render(request, 'cars/cars.html')

def car_detail(request, id):
  # return HttpResponse('<h3>Car detail %s</h3>' % pk)
  single_car = get_object_or_404(Car, pk=id)
  ctx = {
    'single_car': single_car,
  }
  return render(request, 'cars/car_detail.html', ctx)