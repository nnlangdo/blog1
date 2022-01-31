from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView
from .models import Post
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticelDetailView(DeleteView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'