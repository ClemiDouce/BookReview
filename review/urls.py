from django.urls import path, include
from . import views

app_name = "review"

urlpatterns = [
    path('', views.index, name="review-index")
]