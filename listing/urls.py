from django.urls import path
from . import views

urlPattern = [
    path('', views.index, name='allListings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]
