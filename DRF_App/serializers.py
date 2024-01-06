from rest_framework import serializers
from .models import Books, Students


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = (
            'book_id',
            'book_name',
            'book_title',
        )


class StudentSerialier(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
