from django.urls import include, path
from . import views

app_name = 'main'

urlpatterns = [
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('directory/', views.directory, name='directory')
]