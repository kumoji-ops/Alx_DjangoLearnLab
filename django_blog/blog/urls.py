from django.urls import path
from .views import home_view, register_view, CustomLoginView, CustomLogoutView, profile_view,  PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', home_view, name='home'), 
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
    
    # Blog posts CRUD
    path('post/', PostListView.as_view(), name='posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-add'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comments/<int:pk>/delete/',CommentDeleteView.as_view(), name='comment-delete'),
]

