from .models import User
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

#this is for serializing user creation data
class UserCreationSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=100)
    phone_number = PhoneNumberField(allow_blank=False)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        username_exits = User.objects.filter(username=attrs['username']).exists()

        if username_exits:
            raise serializers.ValidationError(detail="This Username already exists!!")
        
        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail="This Email already exists!!")
        
        phone_number_exists = User.objects.filter(phone_number=attrs['phone_number']).exists()

        if phone_number_exists:
            raise serializers.ValidationError(detail="This Phone number already exists")
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user