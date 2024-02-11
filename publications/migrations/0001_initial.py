# Generated by Django 5.0.1 on 2024-01-20 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.TextField()),
                ('publication_date', models.DateField()),
                ('published_in', models.CharField(max_length=200)),
                ('abstract', models.TextField()),
                ('keywords', models.CharField(blank=True, max_length=200)),
                ('publication_link', models.URLField(blank=True)),
                ('doi', models.CharField(blank=True, max_length=100)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='publication_pdfs/')),
            ],
        ),
    ]
