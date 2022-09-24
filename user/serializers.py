from dataclasses import fields
from rest_framework import serializers

from user.models import User as UserModel


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=UserModel
        fields= ["id", "username", "fullname", "ip_address", "join_date",
                 "is_active", "is_admin",]
        
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        password = user.password
        user.set_password(password)
        user.save()
        return user