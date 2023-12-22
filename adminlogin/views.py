from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Book
from django.contrib.auth import logout
from django.contrib import messages
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
        return reverse_lazy('adminhomepage') 

def adminhomepage(req):
    return render(req,'adminhomepage.html')
   
def addbook(request):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']

        books = Book.objects.create(name=name, author=author, isbn=isbn, category=category)
        books.save()
        messages.success(request, 'New Book added successfully.')

        # Redirect to the same page to display the message
        return redirect('addbook')  #
        
    return render(request, "addbook.html")

 
  


def adduser(req):
    return render(req,'adduser.html')

from .models import CreateNewUser

def create_new_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Create a new user
        savedata= CreateNewUser.objects.create(username=username, password=password)
        savedata.save()
        total_users = CreateNewUser.objects.count()
        return render(request, 'adduser.html', {'total_users': total_users, 'shows': savedata})
 
def logout1(request):
    logout(request)
    # Redirect to the homepage or any other desired page after logout
    return redirect('homepage')
def showuser(req):
    return render(req,'showuser.html')

def showbook(request):
    # Retrieve all books from the database
    books = Book.objects.all()

    return render(request, "showbook.html", {'books': books})