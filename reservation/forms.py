from django import forms
from .models import Reservation

# Automatic generate a reservation form to enable automatic validation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_name', 'reservation_email', 'phone_number',
                  'number_people', 'reservation_date', 'reservation_time']

        widgets = {'reservation_date': forms.DateInput(
            attrs={'type': 'date', 'class': 'datepicker'})}
