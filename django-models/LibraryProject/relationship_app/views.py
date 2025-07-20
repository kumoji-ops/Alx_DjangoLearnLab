from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UserCreationForm

from .models import Book, Library

# Book list
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library'

# Login
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Logout
def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

# Register
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})



