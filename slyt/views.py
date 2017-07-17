from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Shortener
from django.http import HttpResponse
from django import forms
from .forms import PostURL
from django.utils import timezone
import string
import random

# Create your views here.

def index(request):
	if request.is_ajax() and request.method == "POST":
		original_url = request.POST['original_url']
		created_date = timezone.now()
		base_url = request.POST['base_url']
		integrity_check = 1
		if not request.POST['custom_tag']:
			while integrity_check >= 1:
				short_url_tag = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
				integrity_check = Shortener.objects.filter(short_url_tag__contains = short_url_tag).count()	
			short_url = base_url + "/" + short_url_tag
			Shortener.objects.create(short_url_tag=short_url_tag,original_url=original_url,custom_tag='',created_date=created_date,short_url=short_url)
			return HttpResponse(short_url)
		else:
			custom_tag = request.POST['custom_tag']
			integrity_check = Shortener.objects.filter(custom_tag__contains = custom_tag).count()
			if integrity_check >= 1:
				return HttpResponse("exists")
			else:
				short_url = base_url + "/" + custom_tag
				Shortener.objects.create(short_url_tag=custom_tag,original_url=original_url,custom_tag=custom_tag,created_date=created_date,short_url=short_url)
				return HttpResponse(short_url)
	else:
		return render(request,'slyt/index.html',{})

def stik_redirect(request,pk):
	handle = get_object_or_404(Shortener, pk=pk)
	return HttpResponseRedirect(Shortener.objects.only('original_url').get(short_url_tag = pk).original_url)