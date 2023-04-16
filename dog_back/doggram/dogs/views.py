from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Achievement, Dog

from .serializers import AchievementSerializer, DogSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = None
