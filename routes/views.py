from django.shortcuts import render

# Create your views here.

from routes.forms import RouteForm


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})
