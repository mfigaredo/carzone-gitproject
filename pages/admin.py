from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

def model_str(obj):
  return str(obj)

model_str.short_description = 'Header'

class TeamAdmin(admin.ModelAdmin):

  def thumbnail(self, object):
    return format_html('<img src="{}" style="width: 60px; border-radius: 20%; "/>'.format(object.photo.url))

  thumbnail.short_description = 'photo'

  list_display = ('id', 'thumbnail',
    'full_name', 
    # '__str__' ,
    # 'first_name', 'last_name', 
    'designation', 'created_date',
    # model_str
    )
  list_display_links = ('full_name', 'thumbnail',  )
  ordering = ('first_name', 'last_name',  )
  search_fields = ('first_name', 'last_name', 'designation', )
  list_filter = ('designation', )

  @admin.display(ordering='first_name', description='Team Full Name')
  def full_name(self, obj):
    # return obj.full_name()
    return f'{obj.first_name} {obj.last_name}'

admin.site.register(Team, TeamAdmin)

