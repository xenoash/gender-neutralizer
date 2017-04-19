from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os, difflib
from polls.models import GenderFile


def upload(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		#fs = FileSystemStorage()
		#filename = fs.save(myfile.name, myfile)
		#uploaded_file_url = fs.url(filename)
		text = extract(myfile)
		
		
		#text = text.replace(gender, neutral.capitalize())
		
		neutral_text = neutralize(text)
		
		#neutral_text = neutral_text.replace(gender, neutral.capitalize())
		
		diff = difflib.ndiff(text.split(' '), neutral_text.split(' '))
		gs_words= ', '.join(x[2:] for x in diff if x.startswith('- '))	#gender-specific words
		
		diff = difflib.ndiff(text.split(' '), neutral_text.split(' '))
		gn_words= ', '.join(y[2:] for y in diff if y.startswith('+ '))	#gender-neutral words
		
		return render(request, 'upload/upload.html', { 
				#'uploaded_file_url': uploaded_file_url,
				#'filename': filename,
				'original_text': text,
				'neutral_text': neutral_text,
				'gs_words': gs_words,
				'gn_words': gn_words,
				})
	else:
		return render(request, 'upload/upload.html')
		
def extract(file):
	lst=[]
	try:
		for chunk in file.chunks():
			lst.append(chunk)
	except:
		return ("Can't open file!")
	text = ''.join(lst)
	return text

	
def neutralize(text):
	'''
	file = open (os.path.join(settings.PROJECT_ROOT,"dictionary.txt"))
	gender_to_neutral = {}
	for line in file:
		line.strip()
		words = line.split(",")
		key = words[0]
		val = words[1]
		val_length=len(val)-1
		value = val[0:val_length]
		gender_to_neutral[key]=value
	file.close()
	'''
	entries = GenderFile.objects.values()
	gender_to_neutral = {}
	for entry in entries:
		key = entry['word']
		value = entry['equivalent']
		gender_to_neutral[key] = value
        
	def replace_all(text, gender_to_neutral):
		for gender, neutral in gender_to_neutral.items():
			text = text.replace(gender, '<'+neutral.capitalize().strip()+'>')
		return text

	try:
		ntext = replace_all(text, gender_to_neutral)
	except:
		return ("Can't process text!")
        
	return ntext