from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import WatchSerializer
from .models import Watch
from utils.permissions import IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin

class WatchViews(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    get_serializer = WatchSerializer
    queryset = Watch.objects.all()

class WatchDetailViews(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin]

    queryset = Watch.objects.all()
    get_serializer = WatchSerializer