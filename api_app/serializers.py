from rest_framework import serializers
from .models import Person, City
from random import choice


class PersonSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(method_name='get_age')

    class Meta:
        model = Person
        fields = '__all__'

    def get_age(self, instance):
        return instance.age


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


