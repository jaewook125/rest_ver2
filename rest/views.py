from django.shortcuts import render, get_object_or_404
from rest.models import Rest

def index(request):
	qs = Rest.objects.all()

	return render(request, 'rest/index.html', {
										"rest":qs,
		})