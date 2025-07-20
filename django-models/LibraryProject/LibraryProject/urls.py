from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('list_books')),  # Redirect root "/" to books
    path('', include('relationship_app.urls')),        # Use URLs from your app
]
