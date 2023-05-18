from django.shortcuts import render, redirect
from .models import Place
from .forms import PlaceForm


def index(request):
    """Home page of remember places."""
    return render(request, 'rp_base/index.html')


def places(request):
    """Displays places list."""
    places = Place.objects.order_by('date_added')
    context = {'places': places}
    return render(request, 'rp_base/places.html', context)


def new_place(request):
    """Creates new place."""
    if request.method != 'POST':
        # Data was not send, create empty form.
        form = PlaceForm()
    else:
        # POST data sent, handle data.
        form = PlaceForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('rp_base:places')
    # Display empty or invalid form.
    context = {'form': form}
    return render(request, 'rp_base/new_place.html', context)
