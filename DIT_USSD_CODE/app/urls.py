from django.urls import path
from . import ussd
urlpatterns = [
path('', ussd.index, name='index')
]
