from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Career

def index(request):
	return render(request,'iml_profile/index.html')

def career_list(request):
	try:
		content_list = Career.objects.order_by('-career_date')[:5]
	except Career.DoesNotExist:
		raise Http404('No Content')
	return render(request,'iml_profile/list.html',\
							{'content_list':content_list})

def contact_me(request):
	return HttpResponse("this is contact page.")

