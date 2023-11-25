import unittest
from .models import Reservation
from .forms import ReservationForm
from django.contrib.auth.models import User
import datetime


class ReservationFormTestCase(unittest.TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='Kewelz10', password='k12345')

    def test_valid_form_data(self):
        # Create a reservation with valid data to see if our form accepts it
        form = ReservationForm({
            'reservation_name': 'Kewel',
            'reservation_email': 'kewel@gmail.com',
            'phone_number': '676452266',
            'number_people': '2',
            'reservation_date':
            datetime.date.today() + datetime.timedelta(days=1),
            'reservation_time': 1,  # which is 09:00am - 11:00am from Models
            'number_of_guests': 2,
        })
        self.assertTrue(form.is_valid())


if __name__ == '__main__':
    unittest.main()
