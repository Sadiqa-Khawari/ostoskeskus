from django.urls import path
from .views import korttilista , uusi_kortti   

urlpatterns = [
    path('', korttilista, name='lista'),
    path('uusikortti', uusi_kortti, name='uusi_kortti'),
]
