from django.shortcuts import render
from .models import Book, Author
from .filters import LastTenDaysFilter
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import models
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [LastTenDaysFilter]


class TopAuthorsViewByLikes(APIView):
    
    def get(self, request):
        top_authors = Author.objects.annotate(
            total_likes = models.Sum('book__likes')
        ).order_by('-total_likes')[:10]
        
        data = []
        for author in top_authors:
            data.append({
                'name': author.name,
                'total_likes': author.total_likes
            })
        
        return Response(data)


class TopAuthorsViewByViews(APIView):
    def get(self, request):
        top_authors = Author.objects.annotate(
            total_vues = models.Sum('book__vues')
        ).order_by('-total_vues')[:10]
        
        data = []
        for author in top_authors:
            data.append({
                'name': author.name,
                'total_likes': author.total_vues
            })
        
        return Response(data)