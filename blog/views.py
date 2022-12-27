from django.shortcuts import render, redirect
from .models import News
from django.utils.cache import cache_page
from django.contrib.auth.decorators import login_required
from .forms import NewsForm
from .utils import send_new_blog_email


@cache_page(60 * 15)
def news_list(request):
    news = News.objects.filter(published=True)
    return render(request, 'blog/news_list.html', {'news': news})


@login_required
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            news.author = request.user
            news.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    if form.is_valid():
            news = form.save()
            news.author = request.user
            news.save()
            cache_page(60 * 15)
            return redirect('news_list')
    if form.is_valid():
            news = form.save()
            news.author = request.user
            news.save()
            cache_page(60 * 15)
            send_new_blog_email(news)
            return redirect('news_list')
    return render(request, 'blog/create_news.html', {'form': form})

    
