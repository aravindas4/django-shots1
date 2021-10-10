from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
