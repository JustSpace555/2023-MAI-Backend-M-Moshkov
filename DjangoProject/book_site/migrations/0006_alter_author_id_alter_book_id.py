# Generated by Django 4.0 on 2023-05-18 16:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('book_site', '0005_alter_author_id_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8f12fdc0-0f18-47fd-91fa-5cf5e8f7acf7'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(default=uuid.UUID('caf23f15-f0da-480e-8b15-1234f4426529'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
