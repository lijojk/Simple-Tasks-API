from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer

# module for token creation /////////////////////////////////////////////////////////////////////////////////
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate

# module for authentication /////////////////////////////////////////////////////////////////////////////////
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# user create ///////////////////////////////////////////////////////////////////////////////////////////////
class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# user display //////////////////////////////////////////////////////////////////////////////////////////////
class UserListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]  # Add TokenAuthentication
    permission_classes = [IsAuthenticated, IsAdminUser]  # Add IsAuthenticated permission
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# for token creation ////////////////////////////////////////////////////////////////////////////////////////
@api_view(['POST'])
def create_token(request):
    user = authenticate(username=request.data['username'], password=request.data['password'])
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)
