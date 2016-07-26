from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):

	#redirect to login if user isn't authenticated

	return render(request, "main/base.html")

def dashboard(request):

		return render(request, "main/base.html")

def properties(request):

	return render (request, "main/properties.html")

def add_properties(request):

	return render (request, "main/properties.html")


def events(request):
	#ajax api for events?
	# returns a list of all of the events?
	pass

def event(request,id):
	# db call to get out specific event to display rendered html to user
	#server side rendering
	pass

def add_event(request):
	#creates a new event. will need to return a server rendered html
	pass


def add_note(request):
    # example from fileupload project
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )
