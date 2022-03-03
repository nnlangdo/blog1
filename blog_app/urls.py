from unicodedata import name
from django.urls import path
# from . import views
from .views import AddCatView,AddCommentView,LikeView,CategoryView, AddPostView, ArticelDetailView, HomeView,DeletePostView, UpdatePostView
urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticelDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCatView.as_view(), name='add_category'),

    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),

]
