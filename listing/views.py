from django.shortcuts import render

# Create your views here.


def index(request):
    render(request, 'listing/allListing.html')


def listing(request):
    render(request, 'listing/listing.html')


def search(request):
    render(request, 'listing/search.html')
