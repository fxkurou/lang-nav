from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .models import Article
from django.utils import translation


def index(request, page_name):
    current_language = translation.get_language()
    articles = Article.objects.all()
    for article in articles:
        translated_field_name = 'content_' + current_language
        translated_content = getattr(article, translated_field_name, '')
        article.content = translated_content
    title = _(page_name.title())
    return render(request, 'content.html', {'title': title, 'article': articles})