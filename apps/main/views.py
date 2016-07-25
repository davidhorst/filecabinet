from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):

	#redirect to login if user isn't authenticated

	return render(request, "main/base.html")

def dashboard(request):

	if request.user.is_authenticated():
		return render(request, "main/index.html")
	else:
		return redirect(reverse('accounts:login'))