# Generated by Django 4.2.1 on 2023-05-18 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_opportunitypost_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarshipPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.FileField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(default='', max_length=50)),
                ('content', models.CharField(max_length=100)),
                ('opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.opportunity')),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.FileField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(default='', max_length=50)),
                ('content', models.CharField(max_length=100)),
                ('opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.opportunity')),
            ],
        ),
        migrations.CreateModel(
            name='InternshipPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.FileField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(default='', max_length=50)),
                ('content', models.CharField(max_length=100)),
                ('opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.opportunity')),
            ],
        ),
    ]
