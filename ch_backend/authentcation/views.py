# views.py

from .models import CustomUser
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate, login
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from django.contrib.auth.hashers import make_password

class UserDetails(APIView):
    def get(self, request):
        user_id = request.GET.get("id")
        users = CustomUser.objects.get(id = user_id)
        serializer = UserRegistrationSerializer(users)
        return  Response(data={"success": True, "status_code": status.HTTP_201_CREATED, "data": serializer.data,
                              "message": "Data Found"}, status=status.HTTP_201_CREATED)
    

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = CustomUser.objects.all()  

    def post(self, request, *args, **kwargs):
        
        request.data['password'] = make_password(request.data['password'])
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            if user:
                refresh = RefreshToken.for_user(user)
                return Response(data={"success": True, "status_code": status.HTTP_201_CREATED, "data": {'refresh': str(refresh), 'access': str(refresh.access_token)},
                              "message": "Data Found"}, status=status.HTTP_201_CREATED)
        return Response(data={"success": False, "status_code": status.HTTP_400_BAD_REQUEST, "data": serializer.errors,
                              "message": "Data Not Found"}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            username = data.get('email')
            password = request.data.get('password')
            user = CustomUser.objects.filter( Q(email=username)).first()

            if not user:
                return Response({
                    "success": False,
                    "error": True,
                    "user_exists": False,
                    'message': "Account not found. Please sign up first."
                }, status=status.HTTP_404_NOT_FOUND)
            
            if user.check_password(password):
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response({
                    'status': status.HTTP_200_OK,
                    'error': False,
                    'message': 'Login successful.',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'role': user.user_role 
                }, status=status.HTTP_200_OK)
            return Response({
                    'status': status.HTTP_200_OK,
                    'error': False,
                    'message': 'Password not match',
                    'role': user.user_role 
                }, status=status.HTTP_200_OK)
            
           

        except CustomUser.DoesNotExist:
            return Response({
                'success': False,
                'error': True,
                'message': 'User not found.',
            }, status=status.HTTP_404_NOT_FOUND)


        except Exception as e:
            return Response({
                "success": False,
                "error": True,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
 
