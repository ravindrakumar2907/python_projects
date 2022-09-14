from rest_framework import serializers
from books.models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title',
                  'author',
                  'quantity',
                  'cost')
        read_only_fields = ('createTimestamp',)
        
        