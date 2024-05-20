from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializer import ArticleSerializer, ArticlesListSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication

# Create your views here.
@api_view(['GET',])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def index(request):
    articles = Article.objects.all()
    serializer = ArticlesListSerializer(articles, many=True)
    return Response(serializer.data)
    # context = {
    #     'articles': articles,
    # }
    # return render(request, 'boards/index.html', context)

@api_view(['POST',])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # if request.method == 'POST':
    #     form = ArticleForm(request.POST)
    #     if form.is_valid():
    #         article = form.save(commit=False)
    #         article.user = request.user
    #         article.save()
    #         return redirect('boards:detail', article.pk)
    # else:
    #     form = ArticleForm()
    # context = {
    #     'form': form
    # }
    # return render(request, 'boards/create.html', context)

@api_view(['GET',])
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
    # article = Article.objects.get(pk=pk)
    # comment_form = CommentForm()
    # comments = article.comment_set.all()
    # context = {
    #     'article': article,
    #     'comment_form': comment_form,
    #     'comments': comments
    # }
    # return render(request, 'boards/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('boards:index')

def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer, status=status.HTTP_201_CREATED)
    # comment = CommentForm(request.POST)
    # if comment.is_valid():
    #     comment = comment.save(commit=False)
    #     comment.article = article
    #     comment.user = request.user
    #     comment.save()
    #     return redirect('boards:detail', article_pk)
    # context = {
    #     'comment': comment
    # }
    # return render(request, 'boards/detail.html', context)

def comment_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    article_pk = comment.article.pk
    comment.delete()
    return redirect('boards:detail', article_pk)