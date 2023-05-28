import json

from django.core.handlers.asgi import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics
from rest_framework.response import Response


@csrf_exempt
@require_http_methods(["GET"])
def search_by_book_title(request: HttpRequest) -> HttpResponse:
    title = request.GET.get("title")
    if title is None:
        return HttpResponseBadRequest(JsonResponse("Title parameter is required"))

    books = Book.objects.filter(title__icontains=title)
    obj = {"content": __format_books__(books)}
    return HttpResponse(JsonResponse(obj))


@csrf_exempt
@require_http_methods(["GET"])
def search_by_author(request: HttpRequest) -> HttpResponse:
    first_name = request.GET.get("first_name")
    last_name = request.GET.get("last_name")
    if first_name is None or last_name is None:
        return HttpResponseBadRequest(JsonResponse("first_name or last_name parameter are missing"))

    author = Author.objects.filter(first_name__exact=first_name, last_name__exact=last_name).first()
    if author is None:
        return HttpResponse(JsonResponse("There is no such author: " + first_name + ' ' + last_name))

    books = Book.objects.filter(author_id=author.id)
    obj = {"content": __format_books__(books)}
    return HttpResponse(JsonResponse(obj))


@csrf_exempt
@require_http_methods(["POST"])
def create_new_author(request: HttpRequest) -> HttpResponse:
    body = __get_request_body__(request)
    first_name = body.get('first_name')
    last_name = body.get('last_name')
    birth_date = body.get('birth_date')
    death_date = body.get('death_date')

    if first_name is None:
        return HttpResponseBadRequest(JsonResponse("Missing first_name"))
    elif last_name is None:
        return HttpResponseBadRequest(JsonResponse("Missing last_name"))
    elif birth_date is None:
        return HttpResponseBadRequest(JsonResponse("Missing birth_date"))

    author = Author.objects.create(
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date,
        death_date=death_date
    )
    return HttpResponse(JsonResponse({"id": str(author.id)}))


@csrf_exempt
@require_http_methods(["POST"])
def create_new_book(request: HttpRequest) -> HttpResponse:
    author_id = request.GET.get("author_id")
    body = __get_request_body__(request)
    title = body.get('title')
    publication_date = body.get('publication_date')

    if author_id is None:
        return HttpResponseBadRequest(JsonResponse("Missing author_id"))
    elif title is None:
        return HttpResponseBadRequest(JsonResponse("Missing title"))
    elif publication_date is None:
        return HttpResponseBadRequest(JsonResponse("Missing publication_date"))

    author = Author.objects.get(pk=author_id)
    if author is None:
        return HttpResponseBadRequest(JsonResponse("Missing author with id = " + str(author_id)))

    book = Book.objects.create(
        title=title,
        author=author,
        publication_date=publication_date,
    )
    return HttpResponse(JsonResponse({"id": str(book.id)}))


def get_all(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        JsonResponse({
            "authors": __format_authors__(Author.objects.all()),
            "books": __format_books__(Book.objects.all())
        })
    )


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def __format_books__(books):
    data = []
    for book in books:
        data.append(book.to_json())
    return data


def __format_authors__(authors):
    data = []
    for author in authors:
        data.append(author.to_json())
    return data


def __get_request_body__(request: HttpRequest):
    body_unicode = request.body.decode('utf-8')
    return json.loads(body_unicode)
