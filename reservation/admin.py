from django.contrib import admin
from .models import Reservation, RestaurantTable

# Register your models here.


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_name', 'reservation_email',
                    'phone_number', 'reservation_date', 'reservation_time', 'reserved_table')


@admin.register(RestaurantTable)
class RestaurantTableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'table_capacity')