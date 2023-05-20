import uuid

from django.db import models


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, unique=True)
    first_name = models.CharField(null=False, max_length=100)
    last_name = models.CharField(null=False, max_length=100)
    birth_date = models.DateField(null=False)
    death_date = models.DateField(null=True)

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        app_label = "book_site"

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

    def to_json(self):
        return {
            "id": str(self.id),
            "first_name": str(self.first_name),
            "last_name": str(self.last_name),
            "birth_date": str(self.birth_date),
            "death_date": str(self.death_date)
        }


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, unique=True)
    title = models.CharField(null=False, max_length=100)
    author = models.ForeignKey(null=False, to=Author, on_delete=models.CASCADE)
    publication_date = models.DateField(null=False)

    class Meta:
        ordering = ["title"]
        verbose_name = ["Book"]
        verbose_name_plural = ["Books"]
        app_label = "book_site"

    def __str__(self):
        return self.title

    def to_json(self):
        return {
            "id": str(self.id),
            "title": str(self.title),
            "author": self.author.to_json(),
            "publication_date": str(self.publication_date)
        }
