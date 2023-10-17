
from django.urls import path
from .views import UserListView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
     path('users/', UserListView.as_view(), name='user-list'),
    
]
