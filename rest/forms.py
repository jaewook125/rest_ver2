from django import forms
from .models import Rest
from rest_ver2.widgets.naver_map_point_widget import NaverMapPointWidget

class RestForm(forms.ModelForm):

	class Meta:
		model = Rest
		field = '__all__'
		widgets = {
			'lnglat': NaverMapPointWidget(attrs={'width': 600, 'height': 300}),
		}