from rest_framework import serializers
from .models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = (
            'book_id',
            'book_name',
            'book_title',
        )