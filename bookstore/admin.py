from django.contrib import admin
from .models import Author , Book , Publisher
from django.contrib.admin import AdminSite

class BookInline(admin.TabularInline):
	model = Book
	extra = 2

class AuthorAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['name']}),
	]
	list_filter = ['name']
	search_fields = ['name']
	list_display = ['name']

class BookAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['name','publisher','authors','translator']}),
		('Advanced options', {'fields':['pages','price'], 'classes':['collapse']}),
	]
	search_fields = ['name','authors','publisher']
	list_display = ['name','pages']
	list_filter = ['name']
class PublisherAdmin(admin.ModelAdmin):
	inlines = [BookInline]
	fields = ['name']
	search_fields = ['name']

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)




