from django.urls import path
from . import views
from .views import CustomLoginView
from .views import create_new_user
urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('adminhomepage/',views.adminhomepage,name='adminhomepage'),
    path('adduser/',views.adduser,name='adduser'),
    path('create_new_user/', create_new_user, name='create_new_user'),
    path('logout/',views.logout1,name='logout'),
    path('showbook/',views.showbook,name='showbook'),
    
    path('showuser/',views.showuser,name='showuser'),
    path('addbook/',views.addbook,name='addbook'),
    
    
]