from rest_framework import serializers

from books.models import BookRecord, Genre


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BookRecord


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = Genre
