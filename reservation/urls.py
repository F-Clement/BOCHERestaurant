from . import views
from django.urls import path

# URL patterns for our views
urlpatterns = [
    path('', views.HomePage.as_view(),
         name='homepage'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('add_reservation', views.AddReservation.as_view(
        success_url="/reservations"), name='new_reservation'),
    path('reservations/', views.ReservationPage.as_view(),
         name='list_reservation'),
    path('edit_reservation/<int:pk>', views.EditReservation.as_view(
        success_url="/reservations"), name='edit_reservation'),
    path('delete_reservation/<int:pk>', views.DeleteReservation.as_view(
        success_url="/reservations"), name='delete_reserv')

]
