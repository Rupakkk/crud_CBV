from rest_framework import serializers
from .models import Student


#Validator
def start_with_r(value): # We can keep any function name 
    if value[0] != 'r' :
        raise serializers.ValidationError('Name must start with R')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50,validators = [start_with_r])
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=50)

    def create(self, validated_data):   # create , post method
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):   # update method
        instance.name = validated_data.get('name',instance.name)
        instance.age = validated_data.get('age',instance.age)
        instance.address = validated_data.get('address',instance.address)
        instance.save()
        return instance

    def validate_age(self,value):   # Field validation
        if value >=200:
            raise serializers.ValidationError('Seat Full')
        return value

    def validate(self, data):    # Object Validation
        nm = data.get('name')
        addr = data.get('address')
        if nm.lower() == 'hawk' and addr.lower() != 'japan':
            raise serializers.ValidationError('City must be Japan')
        return data

  