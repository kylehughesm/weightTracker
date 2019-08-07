from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('entry/', views.enter_weight, name='entry'),
    path('history/', views.history, name='history')
]
