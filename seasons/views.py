from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin
from .models import Season
from .serializers import SeasonSerializer

class SeasonsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class SeasonDetailViews(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin]

    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
