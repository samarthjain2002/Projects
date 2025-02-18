from rest_framework.views import APIView
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, TaskSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from core.models import Task

from django.shortcuts import render
from django.conf import settings
from rest_framework.pagination import PageNumberPagination


User = settings.AUTH_USER_MODEL

class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    """
    def get(self, request):
        '''Render an HTML form for user registration'''
        return render(request, "register.html")
    """
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    """
    def get(self, request):
        '''Render an HTML form for user registration'''
        return render(request, "login.html")
    """
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(email=serializer.validated_data["email"], password=serializer.validated_data["password"])
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Return to-do tasks for the current user.
        """
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """
        Save the task with the current user as the owner.
        """
        serializer.save(user=self.request.user)
    
    def get(self, request, *args, **kwargs):
        """
        Override the get method to handle pagination.
        """
        # Custom pagination handling
        page = request.query_params.get('page', 1)  # Default page is 1
        limit = request.query_params.get('limit', 10)  # Default limit is 10
        paginator = PageNumberPagination()
        paginator.page_size = int(limit)
        
        # Get the queryset for the current user
        tasks = self.get_queryset()
        
        # Paginate the queryset
        result_page = paginator.paginate_queryset(tasks, request)
        
        # Serialize the data
        serializer = self.get_serializer(result_page, many=True)
        
        # Return paginated response with additional metadata
        return paginator.get_paginated_response({
            'data': serializer.data,
            'page': page,
            'limit': limit,
            'total': tasks.count(),
        })

class TaksDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class ResetTokenView(APIView):
    def post(self, request):
        # Old token is deleted
        Token.objects.filter(user=request.user).delete()
        # New token is created
        token, _ = Token.objects.get_or_create(user=request.user)
        # Return the new token
        return Response({"token": token.key})

class LogoutView(APIView):
    def post(self, request):
        # Delete the token
        Token.objects.filter(user=request.user).delete()
        return Response({"detail": "Successfully logged out."})