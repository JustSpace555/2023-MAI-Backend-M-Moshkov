from django.urls import path
from .views import *

urlpatterns = [
    path("api//", get_all, name="get-all"),
    path("api/author/search", search_by_author, name="search-by-author"),
    path("api/author/create", create_new_author, name="create-author"),
    path("api/author/all", AuthorList.as_view(), name="author-list"),
    path("api/author/<int:pk>", AuthorDetail.as_view(), name="author-detail"),
    path("api/book/search", search_by_book_title, name="search-by-book"),
    path("api/book/create", create_new_book, name="create-book"),
    path("api/book/all", BookList.as_view(), name="book-list"),
    path("api/book/<int:pk>", BookDetail.as_view(), name="book-detail")
]
