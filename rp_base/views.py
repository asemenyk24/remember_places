from django.shortcuts import render


def index(request):
    """Home page of remember places."""
    return render(request, 'rp_base/index.html')
