# Generated by Django 5.1.4 on 2025-01-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='images',
            field=models.ImageField(blank=True, default='book_default.png', upload_to=''),
        ),
    ]