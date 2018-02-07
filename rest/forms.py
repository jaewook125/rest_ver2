from django import forms
from .models import Rest
from django.core.validators import RegexValidator
from rest_ver2.widgets.naver_map_point_widget import NaverMapPointWidget

class PostForm(forms.Form):
    point = forms.CharField(validators=[RegexValidator(r'^[+-]?[\d\.]+,[+-]?[\d\.]+$')], widget=NaverMapPointWidget)

    class meta:
    	model = Rest
    	field = '__all__'