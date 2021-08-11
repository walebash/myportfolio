from django.shortcuts import render

from .forms import ClientForm

from . models import Client

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login')
    else:
        form = ClientForm
    return render(request, 'home/register.html', {'form': form})