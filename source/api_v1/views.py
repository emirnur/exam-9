from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import CommentSerializer
from webapp.models import Comment


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.none()
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Comment.objects.all()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        else:
            return [DjangoModelPermissions()]

    @action(methods=['post'], detail=True)
    def like_up(self, request, pk=None):
        photo = self.get_object()
        photo.like_count += 1
        photo.save()
        return Response({'id': photo.pk, 'like_count': photo.like_count})

    @action(methods=['post'], detail=True)
    def like_down(self, request, pk=None):
        photo = self.get_object()
        photo.like_count -= 1
        photo.save()
        return Response({'id': photo.pk, 'like_count': photo.like_count})


