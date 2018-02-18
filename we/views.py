from django.shortcuts import render
from we.models import *


def we(request, news_id):
    we = We.objects.get(id=we_id)

    return render(request, 'landing/we.html', locals())