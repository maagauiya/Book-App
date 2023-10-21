# Generated by Django 4.1.2 on 2023-10-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Last Name')),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Patronymic')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
    ]
