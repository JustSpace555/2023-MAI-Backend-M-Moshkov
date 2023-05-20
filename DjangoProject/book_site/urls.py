from django.urls import path
from .views import *

urlpatterns = [
    path("api//", get_all, name="get-all"),
    path("api/search/book", search_by_book_title, name="search-by-book"),
    path("api/search/author", search_by_author, name="search-by-author"),
    path("api/create/author", create_new_author, name="create-author"),
    path("api/create/book", create_new_book, name="create-book"),
]
