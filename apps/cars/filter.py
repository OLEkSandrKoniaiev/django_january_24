from django_filters import rest_framework as filters

from apps.cars.choices.body_type_choices import BodyTypeChoices
from apps.cars.models import CarModel


class CarFilter(filters.FilterSet):
    year_gtd = filters.NumberFilter(field_name='year', lookup_expr='gte')
    year_range = filters.RangeFilter(field_name='year')
    year_in = filters.BaseInFilter(field_name='year')
    body = filters.ChoiceFilter(field_name='body_type', choices=BodyTypeChoices.choices)
    order = filters.OrderingFilter(
        fields=(
            'brand',
            'price',
            ('id', 'asd')  # випадок коли хочемо назвати параметр сортування власною назвою
        )
    )
