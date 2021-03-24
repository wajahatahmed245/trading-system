from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.log_in, name='login'),
    path('welcome/', views.logout_page, name='logout'),

]
