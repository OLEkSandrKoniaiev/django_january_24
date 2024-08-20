from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel


class AutoParkModel(BaseModel):
    class Meta:
        db_table = 'auto_parks'
        ordering = ['id']

    name = models.CharField(max_length=20, validators=(
        V.RegexValidator(*RegexEnum.AUTO_PARK_NAME.value),
    ))

