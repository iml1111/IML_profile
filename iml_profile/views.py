from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Career
from .models import Award

def index(request):
	try:
		content_list = Career.objects.order_by('-career_date')[:5]
		award_list =Award.objects.order_by('-career_date')[:5]
	except Career.DoesNotExist:
		raise Http404('No Content')
	return render(request,'iml_profile/index.html',\
							{'content_list':content_list,'award_list':award_list})

def career_list(request):
	try:
		content_list = Career.objects.order_by('-career_date')[:5]
	except Career.DoesNotExist:
		raise Http404('No Content')
	return render(request,'iml_profile/list.html',\
							{'content_list':content_list})

def award_list(request):
	try:
		content_list =Award.objects.order_by('-career_date')[:5]
	except Award.DoesNotExist:
		raise Http404('No Content')
	return render(request,'iml_profile/award.html',\
							{'content_list':content_list})

