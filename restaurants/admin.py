from django.contrib import admin
from .models import Restaurant

# Register your models here.

# TO CUSTOMIZE ADMIN FIELDS:
@admin.site.register(Restaurant)
class RestaurantAdmin(admin.Model(Admin)):
    fields = ("name", "opening_time")

# TO RUN THE ADMIN FIELD REGULARLY (WITHOUT MANIPULATION):
# admin.site.register(Restaurant)