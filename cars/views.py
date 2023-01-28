from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Car
from django.db.models import Q, CharField, Value
from django.db.models.functions import Concat

# Create your views here.
def cars(request):
  cars = Car.objects.order_by('-created_date')
  paginator = Paginator(cars, 4)
  page = request.GET.get('page')
  paged_cars = paginator.get_page(page)
  # print(paged_cars)
  ctx = {
    'cars': paged_cars,
    'attribute_search': Car.attribute_values_search(),
  }
  return render(request, 'cars/cars.html', ctx)

def car_detail(request, id):
  # return HttpResponse('<h3>Car detail %s</h3>' % pk)
  single_car = get_object_or_404(Car, pk=id)
  ctx = {
    'single_car': single_car,
  }
  return render(request, 'cars/car_detail.html', ctx)

def search(request):
  # cars = Car.objects.order_by('-created_date')
  cars = Car.objects.annotate(location_search=Concat('city', Value(', '), 'state', output_field=CharField())).order_by('-created_date')
  # if 'keyword' in request.GET:
  #   keyword = request.GET.get('keyword')
  if request.GET.get('keyword', None):
    cars = cars.filter(
      Q(description__icontains=request.GET['keyword']) | 
      Q(car_title__icontains  =request.GET['keyword'])
    )
  
  if request.GET.get('model', None):
    cars = cars.filter(model__iexact=request.GET['model'])

  if request.GET.get('location', None):
    cars = cars.filter(location_search__iexact=request.GET['location'])

  if request.GET.get('year', None):
    cars = cars.filter(year=request.GET['year'])

  if request.GET.get('body_style', None):
    cars = cars.filter(body_style__iexact=request.GET['body_style'])

  if request.GET.get('min_price', None):
    cars = cars.filter(price__gte=int(request.GET['min_price']))

  if request.GET.get('max_price', None):
    cars = cars.filter(price__lte=int(request.GET['max_price']))


  ctx = {
    'cars': cars,
    # 'model_search': Car.attribute_search('model'),
    # # 'city_search': Car.attribute_search('city'),
    # 'location_search': Car.location_search(),
    # 'year_search': Car.attribute_search('year'),
    # 'body_style_search': Car.attribute_search('body_style'),
    # 'transmission_search': Car.attribute_search('transmission'),
    'attribute_search': Car.attribute_values_search(),
  }
  return render(request, 'cars/search.html', ctx)