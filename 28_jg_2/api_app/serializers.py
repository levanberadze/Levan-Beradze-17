import datetime
from rest_framework import serializers
from .models import Person, City
from random import choice
from datetime import date


class PersonSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(method_name='get_age')

    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ['create_date']

    def get_age(self, instance):
        return instance.age

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError()
        return value.lower()

    def validate_gender(self, value):
        return value.lower()

    def validate_birth_date(self, value):
        if isinstance(value, datetime.datetime):
            value = value.date()
        if value > date.today():
            raise serializers.ValidationError('Birth Date Cannot Be A Future Date')
        return value

    def create(self, validated_data):
        if 'city' not in validated_data:
            city = City.objects.first()
            if not City:
                city = City.objects.create(name='Default', zip=0000)
            validated_data['city'] = City
        return super().create(validated_data)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        read_only_fields = ['zip']

    @staticmethod
    def generate_zip():
        zip_nums = []
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for _ in range(4):
            zip_nums.append(str(choice(numbers)))
        return ''.join(zip_nums)

    def create(self, validated_data):
        validated_data['zip'] = self.generate_zip()
        return super().create(validated_data)
