from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({"message": "User already exists"}, status=400)
        User.objects.create_user(username=username, password=password)
        return Response({"message": "Signup successful"}, status=201)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({"message": "Login successful"})
        return Response({"message": "Invalid credentials"}, status=401)
