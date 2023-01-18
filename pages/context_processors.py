
def menu(request):
  menu = [
    ('home', 'Home'), 
    ('cars', 'Cars'), 
    ('about', 'About Us'), 
    ('services', 'Our Services'), 
    ('contact', 'Contact Us'), 
  ]
  return {
    'menu': menu,
  }