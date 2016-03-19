from django.shortcuts import render

def home(request):
	return render(request, 'core/home.html')
	
def news(request):
	return render(request, 'core/news.html')

def contact(request):
	return render(request, 'core/contact.html')

def photos(request):
	return render(request, 'core/photos.html')

def donation(request):
	return render(request, 'core/donation.html')
