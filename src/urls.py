
from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "website"

urlpatterns = [
    path('flux/', views.FluxView.as_view(), name="flux"),
    path('abonnement/', views.AbonnementView.as_view(), name="abonnement"),
    path('review/', include('review.urls')),
    path('ticket/', include('ticket.urls')),
    path('compte/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
