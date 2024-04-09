from rest_framework import serializers
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'Cedula_persona', 'Edad_persona', 'Telefono_persona','Rol_persona', 'first_name', 'last_name']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

#Aca vamos a crear una clase que va a retornar todo menos el password.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'Cedula_persona', 'Edad_persona', 'Telefono_persona',
                  'Rol_persona', 'first_name', 'last_name']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #Datos que va a poder actualizar
        fields = ['first_name', 'last_name', 'Cedula_persona', 'Edad_persona', 'Telefono_persona']