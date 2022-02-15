from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login, name='login'),
    path('change-pw/<token>', views.changePassword, name='changePassword'),
    path('reset-pw', views.resetPassword, name='resetPassword')
]
