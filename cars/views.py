from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cars(request):
  return render(request, 'cars/cars.html')

def car_detail(request, pk):
  return HttpResponse('<h3>Car detail %s</h3>' % pk)