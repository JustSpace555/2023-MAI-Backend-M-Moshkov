# Generated by Django 4.0 on 2023-05-17 19:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('5e9dec7d-2c35-41eb-b5ba-3397418ca60c'), editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField(null=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('4599c167-5d73-4d8a-bde2-acbb1ed3c211'), editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_site.author')),
            ],
            options={
                'verbose_name': ['Book'],
                'verbose_name_plural': ['Books'],
                'ordering': ['title'],
            },
        ),
    ]