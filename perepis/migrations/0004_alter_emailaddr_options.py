# Generated by Django 4.0.1 on 2022-01-16 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perepis', '0003_emailaddr_alter_reviews_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailaddr',
            options={'verbose_name': 'Email', 'verbose_name_plural': 'Emails'},
        ),
    ]