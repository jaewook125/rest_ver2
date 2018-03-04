import re
from django import forms
from django.conf import settings
from django.template.loader import render_to_string

class NaverMapPointWidget(forms.TextInput):
	def render(self,name,value, attrs=None):
		context = dict(attrs, **self.attrs)

		context['naver_client_id'] = settings.NAVER_CLIENT_ID


		rendered = super(NaverMapPointWidget, self).render(name,value, attrs)
		html = render_to_string('widgets/naver_map_point_widget.html', context)

		return rendered + html