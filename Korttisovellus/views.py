from django.shortcuts import render, redirect
from .models import Card
from .forms import CardForm



def card_list(request):
    cards = Card.objects.all()
    return render(request, 'card/card_list.html', {'cards': cards})


def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = CardForm()
    return render(request, 'card/add_card.html', {'form': form})


