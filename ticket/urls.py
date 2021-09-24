from django.urls import path
from . import views

app_name = "ticket"

urlpatterns = [
    path('', views.ListTicketView.as_view(), name="ticket-index"),
    path('create/', views.CreateTicketView.as_view(), name="create-ticket"),
    path('<int:pk>/delete/', views.DeleteTicketView.as_view(), name="delete-ticket"),
    path('<int:pk>/update/', views.UpdateTicketView.as_view(), name="update-ticket"),
    path('<int:pk>/detail/', views.DetailTicket.as_view(), name="detail-ticket"),
]