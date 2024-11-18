from rest_framework import serializers

from .models import Product

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        
        fields = ['id', 'name', 'description', 'price']
        
class RegistrationSerializer(serializers.ModelSerializer):
    
    username = serializers.EmailField()
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)
    
    class Meta:
        model = User
        
        fields = ['username', 'password', 'password2']
        
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        
        user = User(
            
            username = self.validated_data['username'],
        )
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            
            raise serializers.ValidationError({'password': 'Sorry, the password did not match'})
        
        user.set_password(password)
        
        user.save()
        
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField(max_length=255)
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data