from django.urls import path
from .views import wedding_card

urlpatterns = [
    path('', wedding_card, name='wedding_card'),
]
