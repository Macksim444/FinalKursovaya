from django.urls import path
from . import views

app_name = 'realtyestateapp'
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
]
