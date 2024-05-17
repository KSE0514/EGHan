from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('comment/create/<int:article_pk>', views.comment_create, name='comment_create'),
    path('comment/delete/<int:comment_pk>', views.comment_delete, name='comment_delete'),
]