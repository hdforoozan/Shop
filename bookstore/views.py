from django.shortcuts import render , get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import Author , Book , Publisher
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class HomePageView(LoginRequiredMixin, TemplateView):
	template_name = 'home.html'

class BookstoreTemplateView(LoginRequiredMixin , TemplateView):
	template_name = 'bookstore.html'

class AuthorListView(ListView):
	model = Author
	template_name = 'bookstore/AuthorListView.html'

class AuthorCreateView(CreateView):
	model = Author
	fields = ['name']

class AuthorDetailView(DetailView):
	model = Author
	context_object_name = 'aut'
	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		author = get_object_or_404(Author,pk=self.kwargs['pk'])
		context['book_list'] = Book.objects.filter(authors__name=author)
		return context

class AuthorUpdateView(UpdateView):
	model = Author
	fields = ['name']
	template_name = 'bookstore/author-edit.html'

class AuthorDeleteView(DeleteView):
	model = Author
	context_object_name = 'aut'
	success_url = reverse_lazy('home')

class BookListView(ListView):
	model = Book
	template_name = 'bookstore/BookListView.html'

class BookDetailView(DetailView):
	model = Book
	context_object_name = 'book'

class BookCreateView(CreateView):
	model = Book
	fields = ['name','authors','publisher','translator','pages']

class BookUpdateView(UpdateView):
	model = Book
	fields = ['authors','publisher', 'translator', 'pages']
	template_name = 'bookstore/book-edit.html'

class BookDeleteView(DeleteView):
	model = Book
	context_object_name = 'book'
	success_url = reverse_lazy('home')

class PublisherListView(ListView):
	model = Publisher
	template_name = 'bookstore/PublisherListView.html'

class PublisherDetailView(DetailView):
	model = Publisher
	context_object_name = 'pub'
	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		publisher = get_object_or_404(Publisher,pk=self.kwargs['pk'])
		context['book_list'] = Book.objects.filter(publisher__name=publisher)
		return context

class PublisherCreateView(CreateView):
	model = Publisher
	fields = ['name']

class PublisherUpdateView(UpdateView):
	model = Publisher
	fields = ['name']
	template_name = 'bookstore/publisher-edit.html'

class PublisherDeleteView(DeleteView):
	model =  Publisher
	context_object_name = 'pub'
	success_url = reverse_lazy('home')
