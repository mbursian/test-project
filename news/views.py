from django.shortcuts import render
from news.models import *


def news(request, news_id):
    news = News.objects.get(id=news_id)

    return render(request, 'news/news.html', locals())