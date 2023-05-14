from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin
from .models import List
from serializers import ListSerializer

class ListsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = List.objects.all()
    serializer_class = ListSerializer

class ListsDetailViews(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin]

    queryset = List.objects.all()
    serializer_class = ListSerializer