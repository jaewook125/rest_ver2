from django.shortcuts import render, get_object_or_404
from rest.models import Rest, RestImage
from .forms import RestForm

def index(request):
	qs = Rest.objects.order_by('?').first()

	form = RestForm()
	return render(request, 'rest/index.html', {
										"rest":qs,
										"form":form,
		})

def index_image(request, pk):
	qs = Rest.objects.order_by('?').first()
	rest_image = get_object_or_404(RestImage, pk=pk)

	return render(request, 'rest/index_image.html',{
										"rest":qs,
										"rest_image":rest_image,
		})