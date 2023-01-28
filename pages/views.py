from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
  teams = Team.objects.all()
  featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
  all_cars = Car.objects.order_by('-created_date')
  data = {
    'teams': teams,
    'featured_cars': featured_cars,
    'all_cars' : all_cars,
    'attribute_search': Car.attribute_values_search(),
  }
  return render(request, 'pages/home.html', data)

def about(request):
  teams = Team.objects.all()
  data = {
    'teams': teams,
    # 'team_list' : ' - '.join(team.first_name + ' ' + team.last_name for team in teams),
  }
  return render(request, 'pages/about.html', data)

def services(request):
  return render(request, 'pages/services.html', {})

def contact(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    phone = request.POST['phone']
    message = request.POST['message']

    email_subject = 'You have a new message from Carzone website regarding %s' % (subject[:20],)
    message_body = f'Name: {name}\n Email: {email}\n Phone: {phone}\n Message: {message}'

    admin_info = User.objects.filter(is_superuser=True).first()

    if admin_info:
      if email and name and subject:
        send_mail(
          email_subject,
          message_body,
          email,
          [admin_info.email],
          fail_silently=False
        )
        messages.success(request, 'Thank you for contacting us! We will get back to you shortly.')
        return redirect('contact')
      messages.error(request, 'There are missing fields in form.')

  return render(request, 'pages/contact.html', {})
