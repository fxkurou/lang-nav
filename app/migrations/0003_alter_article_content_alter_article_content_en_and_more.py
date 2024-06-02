# Generated by Django 4.2.13 on 2024-06-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_article_content_en_article_content_es_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content_en',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content_es',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content_fr',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_es',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_fr',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
    ]