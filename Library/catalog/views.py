from django.shortcuts import render
from .models import Book, Writer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import generic




def index(request):
    """
    View function for home page of site.
    """
   
    num_books=Book.objects.all().count(),
    num_writers=Writer.objects.count()  
    
    
    return render(
        request,
        'catalog/index.html',
      

       context={'num_books':num_books,'num_writers':num_writers},
    )

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'catalog/signup.html', {'form': form})

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  
    queryset = Book.objects.all()[:5]


class BookDetailView(generic.DetailView):
    model = Book

class WriterListView(generic.ListView):
    model = Writer
    context_object_name = 'writer_list'   
    queryset = Writer.objects.all()[:5] 
class WriterDetailView(generic.DetailView):
    model = Writer
