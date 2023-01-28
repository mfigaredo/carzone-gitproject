from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):

  def thumbnail(self, object):
    return format_html('<img src="{}" style="width: 60px; border-radius: 20%; "/>'.format(object.car_photo.url))

  thumbnail.short_description = 'car image'

  list_display = ('id', 'thumbnail', 'car_title', 'location', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured', )
  list_display_links = ('car_title', 'thumbnail',  )
  list_editable = ('is_featured', )
  search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type', 'state', )
  list_filter = ('city', 'model', 'body_style', 'fuel_type', )

  # def location(self, obj):
  #   return f'{obj.city}, {obj.state}'


admin.site.register(Car, CarAdmin)