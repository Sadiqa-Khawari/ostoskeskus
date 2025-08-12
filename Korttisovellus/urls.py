from django.urls import path
from .views import korttilista , add_card   

urlpatterns = [
    path('', korttilista, name='lista'),
    path('add/', add_card, name='add_card'),
]
