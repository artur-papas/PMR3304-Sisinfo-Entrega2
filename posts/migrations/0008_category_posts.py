# Generated by Django 4.2.7 on 2023-11-23 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_category_related_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(to='posts.post'),
        ),
    ]
