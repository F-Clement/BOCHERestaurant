from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime


# Available times users can select for their reservations

RESERVED_TIME = ((1, "09:00am - 11:00am"), (2, "11:00am - 13:00pm"),
                 (3, "13:00pm - 15:00pm"), (4, "15:00pm - 17:00pm"),
                 (5, "17:00pm - 21:00pm"))


def validate_date(date):
    if date < datetime.date.today():
        raise ValidationError("Date cannot be in the past.")

def validate_npeople(npeople):
    if npeople < 1:
        raise ValidationError("Number of people cannot be less than one.")
    if npeople > 5:
        raise ValidationError("Number of people cannot be greater than five.")

def validate_name(res_name):
    if len(res_name) < 3:
        raise ValidationError("Name cannot be less than three characters.")


# Reservation Models for our database.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_name = models.CharField(max_length=20, validators=[validate_name])
    reservation_email = models.EmailField(max_length=70)
    phone_number = models.IntegerField()
    number_people = models.IntegerField(validators=[validate_npeople])
    reservation_date = models.DateField(validators=[validate_date])
    reservation_time = models.IntegerField(choices=RESERVED_TIME, default=1)
    datetime_created = models.DateTimeField(auto_now_add=True)
    reserved_table = models.ForeignKey(
        'RestaurantTable', on_delete=models.CASCADE)

    def __str__(self):
        return self.reservation_name + " at " + str(self.reservation_date) + \
            " " + str(self.reservation_time)

    def reserve_time(self):
        return RESERVED_TIME[self.reservation_time][1]

#  A table model to be used to verify available space and avoid over booking
# when making reservations.


class RestaurantTable(models.Model):
    table_number = models.IntegerField(unique=True)
    table_capacity = models.IntegerField(default=2)

    def __str__(self):
        return str(self.table_number)
