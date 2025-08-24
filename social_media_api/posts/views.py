from rest_framework import viewsets, permissions, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from notifications.models import Notification 
CustomUser = get_user_model()


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    request.user.following.add(target_user)
    return Response({"status": f"You are now following {target_user.username}"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    request.user.following.remove(target_user)
    return Response({"status": f"You unfollowed {target_user.username}"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed(request):
    user = request.user
    following_users = user.following.all()  # store following users in a variable
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if created:
        Notification.objects.create(
            user=post.author,
            message=f"{request.user.username} liked your post '{post.title}'"
        )
        return Response({"status": "Post liked"})
    else:
        return Response({"status": "Already liked"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post).first()
    
    if like:
        like.delete()
        Notification.objects.create(
            user=post.author,
            message=f"{request.user.username} unliked your post '{post.title}'"
        )
        return Response({"status": "Post unliked"})
    else:
        return Response({"status": "You have not liked this post"})