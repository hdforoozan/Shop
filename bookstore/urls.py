from django.urls import path
from bookstore.views import *
from . import views

app_name = 'bookstore'
urlpatterns = [
	path('', BookstoreTemplateView.as_view(), name ='bookstore'),
	path('authors/', AuthorListView.as_view(), name='authors'),
	path('publishers/', PublisherListView.as_view(), name='publishers'),
	path('books/', BookListView.as_view(), name='books'),
	path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
	path('publishers/<int:pk>', PublisherDetailView.as_view(), name='publisher-detail'),
	path('authors/<int:pk>/' , AuthorDetailView.as_view(), name='author-detail'),
	path('authors/new/', AuthorCreateView.as_view() , name = 'author-new'),
	path('publishers/new/', PublisherCreateView.as_view(), name='publisher-new'),
	path('books/new/', BookCreateView.as_view(), name='book-new'),
	path('authors/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author-edit'),
	path('publisher/<int:pk>/edit/', PublisherUpdateView.as_view(), name='publisher-edit'),
	path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
	path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name = 'author-delete'),
	path('publishers/<int:pk>/delete/', PublisherDeleteView.as_view(), name = 'publisher-delete'),
	path('books/<int:pk>/delete/', BookDeleteView.as_view(), name = 'book-delete'),
]
