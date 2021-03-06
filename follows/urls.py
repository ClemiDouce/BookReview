from django.urls import path

from . import views

app_name = "follows"

urlpatterns = [
    path('', views.AbonnementView.as_view(), name="abonnement"),
    path('<int:pk>/delete/', views.UnfollowView.as_view(), name="unfollow"),
]
