from rest_framework import generics
from .serializers import BookSerializer, GenreSerializer
from books.models import BookRecord, Genre


class BookList(generics.ListCreateAPIView):
    queryset = BookRecord.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookRecord.objects.all()
    serializer_class = BookSerializer
