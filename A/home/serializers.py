from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'age', 'email',)

        extra_kwargs = {
            'email': {'write_only': True}
            
        }
   
    def validate_name(self, value):
        if value == 'admin' :
            raise serializers.ValidationError('name cant be admin')
        return value
            
