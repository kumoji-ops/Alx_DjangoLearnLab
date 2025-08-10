from django.db import models
from datetime import datetime

class Author(models.Model):
    """
    Author model stores basic author information.
    One Author can be linked to multiple Books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model stores title, publication year, and a reference to the Author.
    This establishes a one-to-many relationship from Author to Book.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


# Create your models here.
