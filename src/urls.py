from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as authview
from . import views
from .forms import UserLoginForm

app_name = "website"

urlpatterns = [
    path('', views.FluxView.as_view(), name="flux"),
    path('abonnement/', include('follows.urls')),
    path('posts/', views.PostsView.as_view(), name="posts"),
    path('review/', include('review.urls')),
    path('ticket/', include('ticket.urls')),
    path('accounts/login/', authview.LoginView.as_view(authentication_form=UserLoginForm), name="login"),
    path('accounts/logout', authview.LogoutView.as_view(), name="logout"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignupView.as_view(), name="signup"),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
