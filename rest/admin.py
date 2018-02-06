from django.contrib import admin
from rest.models import Rest, RestImage

class RestImageInline(admin.TabularInline):
	model = RestImage

class RestAdmin(admin.ModelAdmin):
	inlines = [
		RestImageInline,
	]

admin.site.register(Rest, RestAdmin)

admin.site.register(RestImage)