from django.shortcuts import render_to_response, render
from polls.models import GenderFile
from polls.forms import GenderForm

def dictionary(request):
    form = GenderForm(request.POST)
    if form.is_valid():
        form.save()
    entries = GenderFile.objects.values()
    templates={'form': form, 'entries': entries}
    return render_to_response("myapp.html", templates)
    # return render(request,"polls/templates/index.html",{'entries': entries})
def response(request):
    gender_to_neutral = GenderFile.objects.values()
    #entries = GenderFile.objects.values()
    #gender_to_neutral
    #for entry in entries:
        #key = entry['word']
        #value = entry['equivalent']
        #gender_to_neutral[key] = value
    return render(request,'index.html',{ 'gender_to_neutral':gender_to_neutral})