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
class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
queryset = Book.objects.filter(title__icontains='first')[:5] # Get 5 books containing the title war    template_name = 'books/book_list.html'  # Specify your own template name/location
class BookDetailView(generic.DetailView):
    model = Book
def book_detail_view(request,pk):
    try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'catalog/book_detail.html',
        # context={'book/':book_id,}
    )
class WriterListView(generic.ListView):
    model = Writer
    context_object_name = 'writer_list'   # your own name for the list as a template variable
queryset = Writer.objects.filter(first_name__icontains='first')[:5] # Get 5 books containing the title war    template_name = 'books/book_list.html'  # Specify your own template name/location
class WriterDetailView(generic.DetailView):
    model = Writer
def writer_detail_view(request,pk):
    try:
        writer_id=Writer.objects.get(pk=pk)
    except Writer.DoesNotExist:
        raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'catalog/book_detail.html',
        # context={'book/':book_id,}
    )
