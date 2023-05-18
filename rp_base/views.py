from django.shortcuts import render
from .models import Place


def index(request):
    """Home page of remember places."""
    return render(request, 'rp_base/index.html')


def places(request):
    """Displays places list."""
    places = Place.objects.order_by('date_added')
    context = {'places': places}
    return render(request, 'rp_base/places.html', context)
