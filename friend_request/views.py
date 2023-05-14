from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin
from .models import FriendRequest
from serializers import FriendRequestSerializer

class FriendRequestView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

class ListsDetailViews(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin]

    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer