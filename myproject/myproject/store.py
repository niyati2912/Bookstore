from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('orders/', views.place_order, name='place-order'),
]
