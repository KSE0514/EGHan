from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'boards/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('boards:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'boards/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'boards/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('boards:index')

def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment = CommentForm(request.POST)
    if comment.is_valid():
        comment = comment.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('boards:detail', article_pk)
    context = {
        'comment': comment
    }
    return render(request, 'boards/detail.html', context)

def comment_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    article_pk = comment.article.pk
    comment.delete()
    return redirect('boards:detail', article_pk)