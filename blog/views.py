from django.shortcuts import render, redirect
from .models import News

from django.contrib.auth.decorators import login_required
from .forms import NewsForm

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
    return render(request, 'blog/create_news.html', {'form': form})
