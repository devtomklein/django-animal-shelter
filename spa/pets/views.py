from django.shortcuts import render
from django.http import HttpResponseRedirect

from models import Profile

import re

def gallery(request):
	currentUrl = request.get_full_path()
	if re.search("adoptable", currentUrl):
		profiles = Profile.objects.all().filter(status="adoptable")
	elif re.search("adopted", currentUrl):
		profiles = Profile.objects.all().filter(status="adopted")
	elif re.search("lost", currentUrl) or re.search("found", currentUrl):
		profiles = Profile.objects.all().filter(status="lost")
		profiles = Profile.objects.all().filter(status="found")
	else:	
		profiles = Profile.objects.objects.all()
		
	return render(request, 'pets/gallery.html', {'currentUrl':currentUrl, 'profiles':profiles})

def show_profile(request, profile_name):
	try:
		profile = Profile.objects.get(pk=profile_name)
	except Profile.DoesNotExist:
		return render(request, "pets/create_profile.html", {"profile_name":profile_name})
	return render(request, "pets/view_profile.html", {"profile_name":profile_name, "profile":profile})	
		
def edit_profile(request, profile_name):
	try:
		profile = Profile.objects.get(pk=profile_name)
		description = profile.description
	except Profile.DoesNotExist:
		description = ""
		return render(request, "pets/edit_profile.html", {"profile_name":profile_name, "profile_description":description})

def save_profile(request, profile_name):
	name        = request.POST["name"] 
	description = request.POST["description"]
	status = request.POST["status"]
	try:
		profile             = Profile.objects.get(pk=profile_name)
		profile.name        = name
		profile.description = description
		profile.status      = status

	except Profile.DoesNotExist:
		profile             = Profile(name=name, description=description, status=status)
	
	profile.save()
	return HttpResponseRedirect("/"+ status + "/" + name)
	#return render(request, "pets/show_profile.html", {"profile_name":profile_name})







