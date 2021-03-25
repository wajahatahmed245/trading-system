from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('signin/', views.log_in, name='login'),
    path('home/', views.home, name='home'),
    path('welcome/', views.logout_page, name='logout'),
    path('faq/', views.faq, name='faq'),

]
