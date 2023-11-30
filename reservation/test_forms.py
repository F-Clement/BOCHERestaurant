from django.test import TestCase
from .models import Reservation, RestaurantTable
from .forms import ReservationForm
from django.contrib.auth.models import User
import datetime


class ReservationFormTestCase(TestCase):

    def setUp(self):

        # Create a user in setUp so that we have a user for every test
        self.user = User.objects.create(
            username='Keww002', password='k12345')

        # Lets create tables as created by the admin in the database
        self.table1 = RestaurantTable.objects.create(
            table_number=1, table_capacity=2)
        self.table2 = RestaurantTable.objects.create(
            table_number=2, table_capacity=2)
        self.table3 = RestaurantTable.objects.create(
            table_number=3, table_capacity=3)
        self.table4 = RestaurantTable.objects.create(
            table_number=4, table_capacity=3)
        self.table5 = RestaurantTable.objects.create(
            table_number=5, table_capacity=5)

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
        # Create a reservation with past date to see if our form accepts it
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
        # Create a reservation with invalid number of people
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
        self.assertEqual(
            form.errors, {'number_people': [
                'Number of people cannot be greater than five.']}
        )

    def test_form_data_with_zero_people(self):
        # Create a reservation for zero number of people
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
        self.assertEqual(
            form.errors, {'number_people': [
                'Number of people cannot be less than one.']}
        )

    def test_form_data_with_short_name(self):
        # Create a reservation with a too short name
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
        self.assertEqual(
            form.errors, {'reservation_name': [
                'Name cannot be less than three characters.']}
        )

    def test_form_data_with_invalid_email(self):
        # Create a reservation with invalid email address
        form = ReservationForm({
            'reservation_name': 'Kewel',
            'reservation_email': 'kewel@',
            'phone_number': '676452266',
            'number_people': '2',
            'reservation_date':
            datetime.date.today() + datetime.timedelta(days=1),
            'reservation_time': 1,  # which is 09:00am - 11:00am from Models
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors, {'reservation_email': [
                'Enter a valid email address.']}
        )

    def test_form_data_with_no_phone_number(self):
        # Create a reservation with invalid email address
        form = ReservationForm({
            'reservation_name': 'Kewel',
            'reservation_email': 'kewel@gmail.com',
            'phone_number': '',
            'number_people': '2',
            'reservation_date':
            datetime.date.today() + datetime.timedelta(days=1),
            'reservation_time': 1,  # which is 09:00am - 11:00am from Models
        })
        self.assertFalse(form.is_valid())

    def test_all_tables_occupied(self):
        # Create five reservations for particular time and day

        Reservation.objects.create(
            user=self.user,
            reservation_name='Kewel1',
            reservation_date=datetime.date.today() + datetime.timedelta(
                days=1),
            reservation_time=3,
            number_people=2,
            phone_number=676452266,
            reserved_table=self.table1

        )

        Reservation.objects.create(
            user=self.user,
            reservation_name='Kewel2',
            reservation_date=datetime.date.today() + datetime.timedelta(
                days=1),
            reservation_time=3,
            number_people=2,
            phone_number=676452266,
            reserved_table=self.table2
        )

        Reservation.objects.create(
            user=self.user,
            reservation_name='Kewel3',
            reservation_date=datetime.date.today() + datetime.timedelta(
                days=1),
            reservation_time=3,
            number_people=2,
            phone_number=676452266,
            reserved_table=self.table3
        )

        Reservation.objects.create(
            user=self.user,
            reservation_name='Kewel4',
            reservation_date=datetime.date.today() + datetime.timedelta(
                days=1),
            reservation_time=3,
            number_people=2,
            phone_number=676452266,
            reserved_table=self.table4
        )

        Reservation.objects.create(
            user=self.user,
            reservation_name='Kewel5',
            reservation_date=datetime.date.today() + datetime.timedelta(
                days=1),
            reservation_time=3,
            number_people=2,
            phone_number=676452266,
            reserved_table=self.table5
        )

        # Now we try to create one more reservation

        form = ReservationForm({
            'reservation_name': 'Kewel',
            'reservation_email': 'kewel@',
            'phone_number': '676452266',
            'number_people': '2',
            'reservation_date':
            datetime.date.today() + datetime.timedelta(days=1),
            'reservation_time': 3,
        })
        self.assertFalse(form.is_valid())
