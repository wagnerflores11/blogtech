from django.shortcuts import render
from .models import News

def news_list(request):
    news = News.objects.filter(published=True)
    return render(request, 'blog/news_list.html', {'news': news})
