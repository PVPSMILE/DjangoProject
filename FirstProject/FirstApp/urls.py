from django.urls import path 
from . import views

urlpatterns = [
    path('books/', views.BooksView.as_view(), name = 'books'),
    path('books/<slug:slug>/', views.BookDetailView.as_view(), name="book_detail"),
]