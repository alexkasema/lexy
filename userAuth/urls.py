from django.urls import path
from . import views

app_name = 'userAuth'

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('user-settings', views.user_settings_view, name='user-settings'),
]