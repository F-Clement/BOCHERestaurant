from django.db import models
from django.contrib.auth.models import User


# Available times users can select for their reservations

RESERVED_TIME = ((1, "09:00am - 11:00am"), (2, "11:00am - 13:00pm"),
                 (3, "13:00pm - 15:00pm"), (4, "15:00pm - 17:00pm"),
                 (5, "17:00pm - 21:00pm"))


# Reservation Models for our database.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_name = models.CharField(max_length=50)
    reservation_email = models.EmailField(max_length=70)
    phone_number = models.IntegerField()
    number_people = models.IntegerField()
    reservation_date = models.DateField()
    reservation_time = models.IntegerField(choices=RESERVED_TIME, default=1)
    datetime_created = models.DateTimeField(auto_now_add=True)
    reserved_table = models.ForeignKey(
        'RestaurantTable', on_delete=models.CASCADE)

    def __str__(self):
        return self.reservation_name + " at " + str(self.reservation_date) + \
            " " + str(self.reservation_time)

    def validate_date(date):
        if date < timezone.now().date():
            raise ValidationError("Date can not be in the past")
#  A table model to be used to verify available space and avoid over booking
# when making reservations.


class RestaurantTable(models.Model):
    table_number = models.IntegerField(unique=True)
    table_capacity = models.IntegerField(default=2)

    def __str__(self):
        return str(self.table_number)
