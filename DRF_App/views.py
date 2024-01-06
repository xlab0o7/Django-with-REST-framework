from django.shortcuts import render
from rest_framework import generics, viewsets

from DRF_App.models import Books, Students
from DRF_App.serializers import BooksSerializer, StudentSerialier

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


class Student(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerialier
