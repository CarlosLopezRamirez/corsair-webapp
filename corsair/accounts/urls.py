from django.urls import include, path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('reset-pw/', views.reset_pw, name='reset-pw'),
    path('register/', views.register, name='register'),
    path('confirm-email/<int:user_id>/', views.send_email, name='send_email'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
