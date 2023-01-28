from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from cars.models import Car
from django.db.models import Subquery, OuterRef
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in.')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid login credentials.')
      return redirect('login')
  return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are successfully logged out.')
    return redirect('login')
  return redirect('home')

def register(request):
  if request.method == 'POST':
    # messages.error(request, 'This is error message')
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    if password == confirm_password:
      if User.objects.filter(username=username).exists():
        messages.error(request, 'Username already exists')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'Email already exists')
          return redirect('register')
        else:
          user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password, email=email)
          user.save()
          auth.login(request, user)
          messages.success(request, 'You are now logged in.')
          return redirect('dashboard')
          # messages.success(request, 'You are registered successfully.')
          # return redirect('login')
    else:
      messages.error(request, 'Password do not match')
      return redirect('register')

  return render(request, 'accounts/register.html')

@login_required(login_url = 'login')
def dashboard(request):
  ctx = {
    'inquiries': Contact.objects.filter(user_id=request.user.id).order_by('-create_date'),
    # 'inquiries': Contact.objects.filter(user_id=request.user.id).annotate(price=Car.objects.filter(id=OuterRef('car_id')).values('price')).order_by('-create_date'),
  }
  return render(request, 'accounts/dashboard.html', ctx)