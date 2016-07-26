from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.contrib.auth.forms import AuthenticationForm


from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, FormView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from .forms import UserCreateForm, UserUpdateForm
from django.contrib.auth.models import User

class RegisterUser(CreateView):

	template_name = 'accounts/register.html'
	form_class = UserCreateForm
	success_url = '/main'

	def post(self, request):
		#testing git
		form = UserCreateForm(request.POST)
		print "post ran"
		if form.is_valid():

			user = form.save()
			print "user saved"
			user = authenticate(username=request.POST['email'], password=request.POST['password1'])

			#log in user
			if user is not None:
				login(request, user)

			# return to home
			return redirect(reverse('main:index'))

		else:

			return render(request, 'accounts/register.html', {'form': form})

class LoginView(FormView):

	template_name = 'accounts/user_login.html'
	success_url = '/'
	form_class = AuthenticationForm

	def form_valid(self, form):
		print "hello"
		login(self.request, form.get_user())
		return super(LoginView, self).form_valid(form)

def logoutView(request):

	logout(request)

	return redirect(reverse('accounts:login'))
