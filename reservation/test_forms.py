import unittest
from .models import Reservation
from .forms import ReservationForm
from django.contrib.auth.models import User
import datetime


class ReservationFormTestCase(unittest.TestCase):

    # def setUp(self):
    #     # Create a user in setUp so that we have a user for every test
    #     self.user = User.objects.create(
    #         username='Ke002', password='k12345')

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
        })
        self.assertTrue(form.is_valid())

    def test_form_data_with_past_date(self):
        # Create a reservation with valid data to see if our form accepts it
        form = ReservationForm({
            'reservation_name': 'Kewel',
            'reservation_email': 'kewel@gmail.com',
            'phone_number': '676452266',
            'number_people': '2',
            'reservation_date':
            datetime.date.today() - datetime.timedelta(days=1),
            'reservation_time': 1,  # which is 09:00am - 11:00am from Models
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors, {'reservation_date': ['Date cannot be in the past.']})

    def test_form_data_with_large_number_of_people(self):
        # Create a reservation with valid data to see if our form accepts it
        form = ReservationForm({
            'reservation_name': 'Kewel',
            'reservation_email': 'kewel@gmail.com',
            'phone_number': '676452266',
            'number_people': '6',
            'reservation_date':
            datetime.date.today() + datetime.timedelta(days=1),
            'reservation_time': 1,  # which is 09:00am - 11:00am from Models
        })
        self.assertFalse(form.is_valid())


    def test_form_data_with_zero_people(self):
        # Create a reservation with valid data to see if our form accepts it
        form = ReservationForm({
            'reservation_name': 'Kewel',
            'reservation_email': 'kewel@gmail.com',
            'phone_number': '676452266',
            'number_people': '0',
            'reservation_date':
            datetime.date.today() + datetime.timedelta(days=1),
            'reservation_time': 1,  # which is 09:00am - 11:00am from Models
        })
        self.assertFalse(form.is_valid())


    def test_form_data_with_short_name(self):
        # Create a reservation with valid data to see if our form accepts it
        form = ReservationForm({
            'reservation_name': 'Ke',
            'reservation_email': 'kewel@gmail.com',
            'phone_number': '676452266',
            'number_people': '2',
            'reservation_date':
            datetime.date.today() + datetime.timedelta(days=1),
            'reservation_time': 1,  # which is 09:00am - 11:00am from Models
        })
        self.assertFalse(form.is_valid())


if __name__ == '__main__':
    unittest.main()
