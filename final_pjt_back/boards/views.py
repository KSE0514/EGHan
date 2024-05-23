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
from django.shortcuts import render

# 챗봇 =====================================================
# Create your views here.
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

openai.api_key = "sk-proj-h93ycbUTNKWIpPWMi36yT3BlbkFJHMkKOepjz6MebPSbbx1y"

# @csrf_exempt
@api_view(['GET',])
def chat(request):
    print(1)
    if request.method == "GET":
        # data = json.loads(request.body)
        data = request.data
        print(data)
        user_content = data.get("message")
        messages = data.get("messages", [])
        print(messages)
        messages.append({"role": "user", "content": f"{user_content}"})
        
        try:
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            assistant_content = completion.choices[0].message["content"].strip()
            messages.append({"role": "assistant", "content": assistant_content})
            return JsonResponse({"response": assistant_content, "messages": messages})
        except openai.error.OpenAIError as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)
# ==========================================================================

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

@api_view(['GET', 'DELETE', 'PUT',])
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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

@api_view(['POST', 'GET',])
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.article = article
            # serializer.save(user=request.user)
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

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

@api_view(['DELETE',])
def comment_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    article_pk = comment.article.pk
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    # return redirect('boards:detail', article_pk)