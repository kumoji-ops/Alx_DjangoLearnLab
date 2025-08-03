from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList
from rest_framework.authtoken.views import obtain_auth_token  # assuming BookList is a ListAPIView

# Set up router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Define URL patterns
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)), 
     path('get-token/', obtain_auth_token, name='get-token'),  # Automatically includes all ViewSet URLs
]
