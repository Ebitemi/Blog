# Generated by Django 4.2.1 on 2023-05-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_jokes_memes_delete_memesjokes_delete_morj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunitypost',
            name='title',
            field=models.TextField(blank=True, default=''),
        ),
    ]