from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(),
         name='homepage'),
    path('add_reservation', views.AddReservation.as_view(
        success_url="/reservations"), name='new reservation'),
    path('reservations/', views.ReservationPage.as_view(), name='list reservation'),


]
