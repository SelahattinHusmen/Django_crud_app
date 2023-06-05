
from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),


    path('', views.home, name="home"),
    path('companies/', views.companies),
    path('added_companies/', views.added_companies, name="added_companies"),
    path('user/<str:pk_test>/', views.user),
    path('add_companies/', views.add_companies, name="add_companies"),
    path('update_companies/<str:pk>', views.update_companies, name="update_companies"),
    path('delete_companies/<str:pk>', views.delete_companies, name="delete_companies"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),





]
