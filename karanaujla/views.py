from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render
from .models import Book

def index(request):
    books = Book.objects.all()
    selected_book = None

    if request.method == 'POST':
        book_id = request.POST.get('book')
        if book_id:
            selected_book = Book.objects.get(id=book_id)
            selected_book.views += 1
            selected_book.save()

    return render(request, 'karanaujla/index.html', {
        'books': books,
        'selected_book': selected_book,
    })
def landing(request):
    if request.user.is_authenticated:
        return redirect('index')  
    return render(request, 'karanaujla/landing.html')  

def landing_page(request):
    return render(request, 'landing.html')

def index(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, 'karanaujla/index.html', {'books': books})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('index')
    return render(request, 'karanaujla/register.html')

def user_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'karanaujla/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        content = request.POST['content']
        Book.objects.create(
            title=title,
            author=author,
            description=description,
            content=content,
            uploaded_by=request.user
        )
        return redirect('index')
    return render(request, 'karanaujla/add_book.html')

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
