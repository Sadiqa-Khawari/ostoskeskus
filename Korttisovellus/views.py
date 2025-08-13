from django.shortcuts import render, redirect
from .models import Kortti
from .forms import Korttilomake



def korttilista(request):
    kortit = Kortti.objects.all()
    return render(request, 'korttisovellus/lista.html', {'kaikkikortit': kortit})


def uusi_kortti(request):
    if request.method == 'POST':
        form = Korttilomake(request.POST)
        if form.is_valid():
            form.save()
            print('Validi lomake')
            return redirect('lista')
    
    return render(request, 'korttisovellus/uusikortti', {'lomake': form})


