# Generated by Django 4.0.6 on 2024-03-08 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_remove_book_b_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.BigIntegerField()),
            ],
        ),
    ]
