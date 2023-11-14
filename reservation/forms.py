from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_name', 'reservation_email', 'phone_number',
                  'number_people', 'reservation_date', 'reservation_time']

        # fields = '__all__'

        widgets = {'reservation_date': forms.DateInput(
            attrs={'type': 'date'})}
