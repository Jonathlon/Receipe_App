# Generated by Django 5.0.1 on 2024-01-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='difficulty',
        ),
        migrations.AddField(
            model_name='recipe',
            name='pictures',
            field=models.ImageField(default='no_picture.jpg', upload_to='recipes'),
        ),
    ]
