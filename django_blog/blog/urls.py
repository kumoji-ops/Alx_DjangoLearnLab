from django.urls import path
from .views import home_view, register_view, CustomLoginView, CustomLogoutView, profile_view,  PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView
from django.contrib.auth import views as auth_views
from . import views
from .views import post_search_view 


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

    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-add'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/',CommentDeleteView.as_view(), name='comment-delete'),


    # Search posts
    path('search/', post_search_view, name='post-search'),
    path('tags/<str:tag_name>/', views.posts_by_tag_view, name='posts-by-tag'),
]

