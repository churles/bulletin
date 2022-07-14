from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Article


# Create your views here.
def top_screen(request):
    articles = Article.objects.all()
    return render(request, 'board/top-screen.html',{
        'articles':articles,
    })

def detail(request, art):
    article = Article.objects.get(id = art)
    return render(request, 'board/detail.html', {
        'article':article,
    })

def create(request):
    if request.method == 'POST':
        article = Article.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
        )
        article.save()
        return redirect('board:top-screen')

    return render(request, 'board/create.html')

def delete(request, art):
    article = Article.objects.get(id = art);
    article.delete()
    return redirect('board:top-screen')

    
def edit(request, art):
    article = Article.objects.get(id = art);
    if request.method == 'POST':
        article.title=request.POST.get('title')
        article.content=request.POST.get('content')
        article.save()
        return redirect('board:top-screen')

    return render(request, 'board/edit.html',{
        'article':article,
    })