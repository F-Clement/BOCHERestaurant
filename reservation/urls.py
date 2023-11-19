from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(),
         name='homepage'),
    path('menu/', views.Menu.as_view(), name='Menu'),
    path('add_reservation', views.AddReservation.as_view(
        success_url="/reservations"), name='new reservation'),
    path('reservations/', views.ReservationPage.as_view(),
         name='list reservation'),
    path('edit_reservation/<int:pk>', views.EditReservation.as_view(
        success_url="/reservations")),
    path('delete_reservation/<int:pk>',
         views.DeleteReservation.as_view(success_url="/reservations"))




]
