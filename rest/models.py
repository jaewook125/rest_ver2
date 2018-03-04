import re
from django.forms import ValidationError
from django.db import models


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')
        #숫자,숫자 형식의 폼으로만 작성가능

class Rest(models.Model):
	name = models.CharField(max_length=100, verbose_name='식당 이름')
	addr = models.TextField(blank=True, verbose_name='주소')

	def __str__(self):
		return self.name

class RestImage(models.Model):
	rest_image = models.ForeignKey(Rest, on_delete=models.CASCADE)
	image = models.ImageField(verbose_name='식당 이미지')