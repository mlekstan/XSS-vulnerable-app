# Generated by Django 5.1.4 on 2024-12-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_comments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]