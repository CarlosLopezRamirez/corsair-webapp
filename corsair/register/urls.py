from django.urls import path
from . import views

app_name = 'register'
urlpatterns = [
    path('', views.register, name='register'),
    path('confirm-email/<token>', views.confirmEmail, name='confirmEmail'),
    path('confirm-email/', views.resendEmail, name='resendEmail')
]
