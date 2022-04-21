from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.age = validated_data.get('age',instance.age)
        instance.address = validated_data.get('address',instance.address)
        instance.save()
        return instance