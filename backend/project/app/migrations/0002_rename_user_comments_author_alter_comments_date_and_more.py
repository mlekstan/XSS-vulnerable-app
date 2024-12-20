# Generated by Django 5.1.4 on 2024-12-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='user',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='title',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
