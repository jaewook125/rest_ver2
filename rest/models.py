from django.db import models

class Rest(models.Model):
	name = models.CharField(max_length=100, verbose_name='식당 이름')
	addr = models.TextField(blank=True, verbose_name='주소')

	def __str__(self):
		return self.name

class RestImage(models.Model):
	rest_image = models.ForeignKey(Rest, on_delete=models.CASCADE)
	image = models.ImageField(verbose_name='식당 이미지')