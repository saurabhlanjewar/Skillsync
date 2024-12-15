from rest_framework import serializers
from django.contrib.auth.models import User
from Group.api.serializers import GroupSerializer
from Task.api.serializers import TaskSerializer


    

class UserSerializers(serializers.ModelSerializer):
    group_list = GroupSerializer(many=True, read_only=True)
    todo = TaskSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'group_list', 'todo']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
    def save(self):

            password = self.validated_data['password']

            if User.objects.filter(email=self.validated_data['email']).exists():
                raise serializers.ValidationError({'error': 'Email already exists!'})

            account = User(email=self.validated_data['email'], username=self.validated_data['username'])
            account.set_password(password)
            account.save()

            return account
            