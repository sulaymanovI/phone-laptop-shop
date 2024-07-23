from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework import generics
from .serializers import *

class SignUpAPIView(APIView):
    permission_classes=[permissions.AllowAny]
    serializer_class=SignUpSerizalier

    def post(self,request,*args, **kwargs):
        email=request.data.get('email',None)
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={"success":True , "message":"You have successfully been registred!"})
    
class LoginView(TokenViewBase):
    serializer_class=LoginSerializer
    permission_classes=[permissions.AllowAny]

class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            RefreshToken(request.data['refresh']).blacklist()
        except TokenError:
            raise ValidationError({'refresh': 'Bad token'})
        data={
            "success":True,
            "message":"You have successfully been logged out"
        }
        return Response(data=data , status=status.HTTP_204_NO_CONTENT)
