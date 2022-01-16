# Generated by Django 4.0.1 on 2022-01-16 15:11

from django.db import migrations, models
import perepis.models


class Migration(migrations.Migration):

    dependencies = [
        ('perepis', '0002_alter_reviews_options_reviews_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAddr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail адресс')),
            ],
        ),
        migrations.AlterField(
            model_name='reviews',
            name='avatar',
            field=models.ImageField(default='perepis/no_avatar.png', upload_to=perepis.models.user_directory_path),
        ),
    ]