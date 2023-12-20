from django.urls import path
from . import views
from .views import CustomLoginView
from .views import create_new_user
urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('adminhomepage/',views.add_book,name='add_book'),
    path('adduser/',views.adduser,name='adduser'),
    path('create_new_user/', create_new_user, name='create_new_user'),
    path('logout/',views.logout1,name='logout'),
    path('showbook/',views.showbook,name='showbook'),
    path('all_books/',views.all_books, name='allbooks'),
    path('add',views.add,name='add'),
    
    
]