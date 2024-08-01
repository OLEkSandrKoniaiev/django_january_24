from rest_framework import serializers
from rest_framework.serializers import ValidationError

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'created_at', 'updated_at')

    # def validate(self, data):
    #     # print(data)
    #     if data['price'] == data['year']:
    #         raise ValidationError({'details': 'Error!! price equals year'})
    #     return super().validate(data)

    def validate_year(self, year: int):
        if year == 2020:
            raise ValidationError({'details': 'Year equals 2020'})
        return year
