from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Reservation, RestaurantTable, RESERVED_TIME
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages


# Create your views here.

class HomePage(generic.TemplateView):
    template_name = "index.html"


class Menu(generic.TemplateView):
    template_name = "menu.html"

@method_decorator(login_required, name='dispatch')
class AddReservation(generic.edit.CreateView):
    template_name = "add_reservation.html"
    form_class = ReservationForm

    def add_reservation(self, request, form):
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('reservations')
        form = ReservationForm()
        context = {
            'form': form
        }

        return render(request, "../templates/add_reservation.html", context)

    def form_valid(self, form):
        form.instance.user = self.request.user
        rdate = form.cleaned_data['reservation_date']
        rtime = form.cleaned_data['reservation_time']
        npeople = form.cleaned_data['number_people']

        reservations_on_requested_date = Reservation.objects.filter(
            reservation_date=rdate, reservation_time=rtime)

        available_tables = list(RestaurantTable.objects.filter(
            table_capacity__gte=npeople
        ).order_by('table_capacity'))

        for reservation in reservations_on_requested_date:
            for atable in available_tables:
                if atable.table_number == reservation.reserved_table.table_number:
                    available_tables.remove(atable)
                    break

        if len(available_tables) > 0:
            form.instance.reserved_table = available_tables[0]
            messages.success(
                self.request,
                f'Booking confirmed for {npeople} people on {rdate} at {RESERVED_TIME[rtime][1]}'
            )
        else:
            messages.error(
                self.request,
                f'No table available for {npeople} people on {rdate} at {RESERVED_TIME[rtime][1]}'
            )

            # form = ReservationForm(initial=reserved)
            context = {
                'form': form
            }

            return render(self.request, "../templates/add_reservation.html", context)

        return super(AddReservation, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ReservationPage(generic.ListView):
    template_name = "reservations.html"
    model = Reservation

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class EditReservation(generic.edit.UpdateView):
    template_name = "edit_reservation.html"
    form_class = ReservationForm
    model = Reservation

    def edit(self, request, reservation_id):
        reserved = get_object_or_404(Reservation, id=reservation_id)
        if request.method == 'POST':
            form = ReservationForm(request.POST, instance=reserved)
            if form.is_valid():
                form.save()
                return redirect('/reservations')
        form = ReservationForm(initial=reserved)
        context = {
            'form': form
        }
        return render(request, "../templates/edit_reservation.html", context)


@method_decorator(login_required, name='dispatch')
class DeleteReservation(generic.edit.DeleteView):
    template_name = "delete_reservation.html"
    model = Reservation

    def delete(self, request, pk):
        delete_reserved = get_object_or_404(Reservation, id=pk)
        delete_reserved.delete()
        return redirect('/reservations')
