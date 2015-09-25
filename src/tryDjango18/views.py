from django.shortcuts import render
# views fora do Django Project

def about(request):
	return render(request, 'about.html', {})