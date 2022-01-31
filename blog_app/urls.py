from unicodedata import name
from django.urls import path
# from . import views
from .views import AddPostView, ArticelDetailView, HomeView,DeleteView
urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticelDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
