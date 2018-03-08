from django.urls import path
from . import views


urlpatterns = [
path('', views.index, name='index'),
path('books/', views.BookListView.as_view(), name='books'),
path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
path('writers/', views.WriterListView.as_view(), name='writers'),
path('writer/<int:pk>', views.WriterDetailView.as_view(), name='writer-detail')

]
