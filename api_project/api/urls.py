from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList  # assuming BookList is a ListAPIView

# Set up router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Define URL patterns
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),  # Automatically includes all ViewSet URLs
]
