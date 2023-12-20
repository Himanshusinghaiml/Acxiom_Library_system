from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Book
from django.contrib.auth import logout
# Create your views here.
def adminlogin(req):
    return render(req,'adminlogin.html')

def homepage(req):
    return render(req,'homepage.html')
def userlogin(req):
    return render(req,'userlogin.html')


# myapp/views.py

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        # Customize the URL where the user is redirected after a successful login
        return reverse_lazy('add_book') 

def adminhomepage(req):
    return render(req,'adminhomepage.html')
   
def add_book(request):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']

        books = Book.objects.create(name=name, author=author, isbn=isbn, category=category)
        books.save()
        alert = True
         
    return render(request, "adminhomepage.html")

 
def add(req):
    return render(req,'addbook1.html') 


def adduser(req):
    return render(req,'adduser.html')

from .models import CreateNewUser

def create_new_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Create a new user
        CreateNewUser.objects.create(username=username, password=password)

        # Redirect to a success page or any other page as needed
        return redirect('add_book')

    return render(request, 'create_new_user.html')
 
def logout1(request):
    logout(request)
    # Redirect to the homepage or any other desired page after logout
    return redirect('homepage')

def showbook(req):
    return render(req,'showbook.html')

def all_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()

    return render(request, "showbook.html", {'books': books})