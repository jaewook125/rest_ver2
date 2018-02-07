from django.shortcuts import render, get_object_or_404
from rest.models import Rest
from .forms import PostForm

def index(request):
	qs = Rest.objects.order_by('?').first()
	form = PostForm()
	return render(request, 'rest/index.html', {
										"rest":qs,
										"form":form,
		})