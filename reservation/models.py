from django.db import models
from django.contrib.auth.models import User


# Available times users can select for their reservations

RESERVED_TIME = ((1, "09:00am - 11:00am"), (2, "11:00am - 13:00pm"),
                 (3, "13:00pm - 15:00pm"), (4, "15:00pm - 17:00pm"),
                 (5, "17:00pm - 21:00pm"))


# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    phone = models.IntegerField()
    number_of_people = models.IntegerField()
    date = models.DateField()
    time = models.TimeField(choices=RESERVED_TIME, default=1)
    time_created = models.DateTimeField(auto_now_add=True)

    # In case a user makes more than one reservation they should follow an order
    class Meta:
        ordering = ['time_created']

    def __str__(self):
        return self.name
