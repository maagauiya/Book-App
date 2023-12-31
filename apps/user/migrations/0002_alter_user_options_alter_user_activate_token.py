# Generated by Django 4.1.2 on 2023-10-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='user',
            name='activate_token',
            field=models.UUIDField(blank=True, null=True, verbose_name='Activation token for account'),
        ),
    ]
