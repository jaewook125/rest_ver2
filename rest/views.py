from django.shortcuts import render, get_object_or_404, render_to_response
from rest.models import Rest, RestImage
from django.conf import settings

def index(request):
	qs = Rest.objects.order_by('?').first()

	return render(request, 'rest/index.html', {
										"rest":qs,
										'NAVER_CLIENT_ID': settings.NAVER_CLIENT_ID,
		})

def index_image(request, pk):
	qs = Rest.objects.all()

	return render(request, 'rest/index_image.html',{
										"rest":qs,
										'NAVER_CLIENT_ID': settings.NAVER_CLIENT_ID,
		})