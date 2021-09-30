from django.urls import path

from . import views

app_name = "review"

urlpatterns = [
    path('', views.ListReviewView, name="review-index"),
    path('create/', views.CreateReviewView.as_view(), name="create-review"),
    path('create/ticket/<int:pk>/', views.CreateReviewOnTicketView.as_view(), name="create-review-ticket"),
    path('create/ticket/', views.CreateReviewAndTicket.as_view(), name="create-review-and-ticket"),
    path('<int:pk>/delete/', views.DeleteReviewView.as_view(), name="delete-review"),
    path('<int:pk>/update/', views.UpdateReviewView.as_view(), name="update-review")
]
