from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
  if request.method == 'POST':
    car_id = request.POST['car_id']
    car_title = request.POST['car_title']
    user_id = request.POST['user_id']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    customer_need = request.POST['customer_need']
    email = request.POST['email']
    phone = request.POST['phone']
    city = request.POST['city']
    state = request.POST['state']
    message = request.POST['message']

    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.filter(car_id=car_id, user_id=user_id).count()
      if has_contacted:
        messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
        return redirect('car_detail', id=car_id)

    contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name, customer_need=customer_need, email=email, phone=phone, city=city, state=state, message=message)

    admin_info = User.objects.filter(is_superuser=True).first()

    if admin_info:
      send_mail(f'New Car Inquiry for car id: {car_id}', 
        f'You have a new inquiry for the car {car_title}. Please login to your admin panel for more info.', 
        settings.EMAIL_HOST_USER, 
        [admin_info.email], 
        fail_silently=False
      )

    contact.save()
    messages.success(request, 'Your inquiry has been submitted, we will get back to you shortly.')

    return redirect('car_detail', id=car_id)
  return

def test(request):
  car_id = 1
  return redirect('car_detail', id=car_id)

