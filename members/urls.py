from unicodedata import name
from django.urls import path
from .views import ShowProfilePageView, UserRegisterView, UserEditView
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),  
]
