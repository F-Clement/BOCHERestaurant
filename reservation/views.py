from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Reservation
from .forms import ReservationForm


# Create your views here.

class HomePage(generic.TemplateView):
    template_name = "index.html"


class AddReservation(generic.edit.CreateView):
    template_name = "add_reservation.html"
    form_class = ReservationForm

    def add_reservation(self, request, form):
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                # form.instance.user = 1
                form.save()
                return redirect('reservations')
        form = ReservationForm()
        context = {
            'form': form
        }

        return render(request, "../templates/add_reservation.html", context)


class ReservationPage(generic.ListView):
    template_name = "reservations.html"
    model = Reservation
