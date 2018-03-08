from django.shortcuts import render
from .models import Book, Writer
from django.views import generic


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count(),
    num_writers=Writer.objects.count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'catalog/index.html',
        # {'catalog':index}

        context={'num_books':num_books,'num_writers':num_writers},
    )

