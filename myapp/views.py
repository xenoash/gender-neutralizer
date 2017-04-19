
from myapp.models import Entry
from myapp.forms import EntryForm

def guestbook(request):
	form=EntryForm(request.POST)
	if form.is_valid():
		form.save()
	entries=Entry.objects.all().order_by("-date")
	templates={'form': form, 'entries': entries}
	return render_to_response("myapp.html", templates)