from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsOwnerOrReadOnly

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['movie_title']
    ordering_fields = ['rating', 'created_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
