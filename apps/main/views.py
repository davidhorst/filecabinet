from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import EventCreateForm
from models import Event
from django.http import HttpResponse

# Create your views here.
def index(request):

	#redirect to login if user isn't authenticated

	return render(request, "main/base.html")

def dashboard(request):

	if request.user.is_authenticated():
		return render(request, "main/event.html")
	else:
		return redirect(reverse('accounts:login'))

def properties(request):

	return render (request, "main/properties.html")

def event(request,id):
	event = Event.objects.get(pk=id)
	context={
	'event':event
	}
	return render(request, 'main/event.html',context)

def events(request):
	events = Event.objects.all()
	context={
	'events':events
	}
	return render(request, 'main/dashboard.html',context)


def add_event(request):
	if request.POST:
		template_name = 'main/add_event.html'
		event_form = EventCreateForm(request.POST)
		#bug create db entry for event here
		if event_form.is_valid:
			return redirect('event_id')
		else:
			print 'didnt work'
			return HttpResponse('didnt create event')
	else:
		template_name = 'main/add_event.html'
		context={
			'form':EventCreateForm()
		}
		return render(request,'main/add_event.html',context)

def note(request,id):
	pass

def notes(request):
	return render(request, 'main/note.html')

def add_note(request,id):
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
