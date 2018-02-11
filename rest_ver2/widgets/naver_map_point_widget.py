import re
from django import forms
from django.conf import settings
from django.template.loader import render_to_string

class NaverMapPointWidget(forms.TextInput):

    html = render_to_string('widgets/naver_map_point_widget.html')