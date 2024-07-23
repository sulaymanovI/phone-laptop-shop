from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

def authenticate_user(request=None, email=None, password=None, **kwargs):
    user = authenticate(email=email, password=password)
    if user is None:
        raise AuthenticationFailed("Kiritilgan ma'lumotlarga ega foydalanuvchi topilmadi !")
    return user

class SignUpSerizalier(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","email","password"]
        
    def create(self,data):
        password=data["password"]
        user=super().create(data)
        user.set_password(password)
        user.save()
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["fullname" , "email" , "user_type"]

class LoginSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls,user):
        return RefreshToken.for_user(user=user)
    
    default_error_messages = {
        "no_account_found" : "Bu ma'lumotga ega aktiv foydalanuvchi topilmadi"
    }

    def validate_user(self,attrs):
        email,password= attrs['email'] , attrs['password']
        self.user=authenticate_user(self.context['request'] , email=email , password=password)
        print(111, self.user)
        if not self.user:
            self.fail("no_active_account")
        return {}
    
    def validate(self,attrs):
        data=self.validate_user(attrs=attrs)
        refresh=self.get_token(self.user)
        data['refresh']=str(refresh)
        data['access']=str(refresh.access_token)
        data['id'] = str(self.user.id)
        
        return data

class LogoutSerializer(serializers.Serializer):
    refresh=serializers.CharField()

    def validate(self, attrs):
        self.token=attrs['refresh']
        return attrs
    
class ResetPasswordEmailSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)
