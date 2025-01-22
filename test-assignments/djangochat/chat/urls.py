from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<int:receiver_id>/', views.start_chat, name='start_chat'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]