from django.shortcuts import render, redirect
from .models import Card
from .forms import CardForm



def korttilista(request):
    cards = Card.objects.all()
    return render(request, 'korttisovellus/lista.html', {'kaikkikortit': cards})


def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('korttilista')
    else:
        form = CardForm()
    return render(request, 'card/add_card.html', {'form': form})


