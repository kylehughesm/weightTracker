from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('<username>/', views.user_account, name='user_account'),
    path('entry/', views.enter_weight, name='entry'),
    path('history/', views.history, name='history')
]
