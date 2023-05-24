from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Place
from .forms import PlaceForm
from django.http import Http404


def index(request):
    """Home page of remember places."""
    return render(request, 'rp_base/index.html')


@login_required
def places(request):
    """Displays places list."""
    places = Place.objects.filter(user = request.user).order_by('date_added')
    context = {'places': places}
    context['count'] = context['places'].count()
    return render(request, 'rp_base/places.html', context)


@login_required
def new_place(request):
    """Creates new place."""
    if request.method != 'POST':
        # Data was not send, create empty form.
        form = PlaceForm()
    else:
        # POST data sent, handle data.
        form = PlaceForm(data = request.POST)
        if form.is_valid():
            new_place = form.save(commit = False)
            new_place.user = request.user
            new_place.save()
            return redirect('rp_base:places')
    # Display empty or invalid form.
    context = {'form': form}
    return render(request, 'rp_base/new_place.html', context)


@login_required
def edit_place(request, place_id):
    """Edit existing place."""
    place = Place.objects.get(id = place_id)
    # Check if theme belongs to its owner.
    if place.user != request.user:
        raise Http404
    if request.method != 'POST':
        # Place exists, fill the form.
        form = PlaceForm(instance = place)
    else:
        # POST data sent, handle data.
        form = PlaceForm(instance = place, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('rp_base:places')
    context = {'place': place, 'form': form}
    return render(request, 'rp_base/edit_place.html', context)


@login_required
def delete_place(request, place_id):
    """Deletes selected place."""
    place = Place.objects.get(id = place_id)
    # Check if theme belongs to its owner.
    if place.user != request.user:
        raise Http404
    if request.method == 'POST':
        place.delete()
        return redirect('rp_base:places')
    context = {'place': place}
    return render(request, 'rp_base/delete_place.html', context)
