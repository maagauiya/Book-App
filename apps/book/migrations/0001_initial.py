# Generated by Django 4.1.2 on 2023-10-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0002_alter_genre_description_alter_genre_name'),
        ('author', '0002_alter_author_first_name_alter_author_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title of the book')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Description of the book')),
                ('average_rating', models.FloatField(default=0, verbose_name='Средний рейтинг')),
                ('authors', models.ManyToManyField(related_name='author_books', to='author.author', verbose_name='Author')),
                ('genres', models.ManyToManyField(related_name='genre_books', to='genre.genre', verbose_name='Genre')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]