# Generated by Django 4.0.2 on 2023-09-20 15:02

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(verbose_name='本文'),
        ),
    ]