from django.shortcuts import render
from rest_framework import generics, viewsets

from DRF_App.models import Books
from DRF_App.serializers import BooksSerializer

# Create your views here.


# class BookList(generics.ListCreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer


# class BookDetail(generics.RetrieveDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer


class Books(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
