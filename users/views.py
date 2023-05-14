from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from .serializers import UserSerializer
from utils.permissions import IsAdminOnlyGET, IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin

class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOnlyGET]

    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"