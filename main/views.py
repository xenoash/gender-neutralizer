from django.http import HttpResponse
from django.shortcuts import render
import cookielib, urllib2
from bs4 import BeautifulSoup, NavigableString
from django.conf import settings
import re, os, json, difflib
from polls.models import GenderFile

def index_view(request):
		return HttpResponse("This is not a valid input. \nPlease enter a text input or a URL that starts with 'http' after the '/' to run the service.")

		
def json_view(request, input):
	if not input.startswith('http'):
		neutral_text = neutralize(input)
				
		diff = difflib.ndiff(input.split(' '), neutral_text.split(' '))
		gs_words= ', '.join(x[2:] for x in diff if x.startswith('- '))	#gender-specific words
		
		diff = difflib.ndiff(input.split(' '), neutral_text.split(' '))
		gn_words= ', '.join(y[2:] for y in diff if y.startswith('+ '))	#gender-neutral words
		
		dict = json.dumps({'response':{'headline': 'None', 'original_text': input, 'neutral_text': neutral_text, 'gender-specific_words': gs_words, 'gender_neutral_words': gn_words}})
		return render(request, 'main/json_view.html', {
				'dict' : dict,
			})
	else:
		url = input
		headline, original_text = extract(url)
		neutral_text = neutralize(original_text)
		#dict = {}
		dict = json.dumps({'response':{'url': url, 'headline': headline, 'original_text': original_text, 'neutral_text': neutral_text}})
		return render(request, 'main/json_view.html', {
				'dict' : dict,
			})

def result_view(request, input):
	if not input.startswith('http'):
		neutral_text = neutralize(input)
		
		
		diff = difflib.ndiff(input.split(' '), neutral_text.split(' '))
		gs_words= ', '.join(x[2:] for x in diff if x.startswith('- '))	#gender-specific words
		
		diff = difflib.ndiff(input.split(' '), neutral_text.split(' '))
		gn_words= ', '.join(y[2:] for y in diff if y.startswith('+ '))	#gender-neutral words


		return render(request, 'main/view.html', {
				'headline': 'User Text',
				'original_text': input,
				'neutral_text': neutral_text,
				'gs_words': gs_words,
				'gn_words': gn_words,
			})
	else:
		url = input
		headline, original_text = extract(url)
		neutral_text = neutralize(original_text)
		lst = []
		diff = difflib.ndiff(original_text.split(' '), neutral_text.split(' '))
		for d in diff:
			lst.append(d)
		diff = ''.join(lst)
		return render(request, 'main/view.html', {
				'headline': headline,
				'original_text': original_text,
				'neutral_text': neutral_text,
				'diff': diff,
			})
		
def extract(url):
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	html = opener.open(url)
	'''with opener.open(url) as url:
		html = url.read()'''
	soup = BeautifulSoup(html, 'html.parser')
	headline = soup.find("h1", id= "headline").string

	# kill all divs that contain ads and unwanted texts
	for div in soup('div', {'id': 'newsletter-promo'}):
		div.decompose()    # rip it out
	
	for ad in soup('div', {'id': 'TopAd'}):
		ad.decompose()    # rip it out
	
	for ad in soup('div', {'id': 'TragedyAd'}):
		ad.decompose()    # rip it out
		
	for ad in soup('div', {'id': 'FlexAd'}):
		ad.decompose()    # rip it out
	
	for ad in soup('div', {'id': 'story-ad-1'}):
		ad.decompose()    # rip it out

	for ad in soup('div', {'id': 'story-ad-2'}):
		ad.decompose()    # rip it out
		
	for ad in soup('div', {'id': 'story-ad-3'}):
		ad.decompose()    # rip it out

	for ad in soup('div', {'id': 'story-ad--aggro-2'}):
		ad.decompose()    # rip it out
		
	for ad in soup('div', {'id': 'story-ad--aggro-4'}):
		ad.decompose()    # rip it out
	
	for ad in soup('div', {'id': 'story-ad--aggro-6'}):
		ad.decompose()    # rip it out
		
	for ad in soup('div', {'id': 'story-ad--aggro-8'}):
		ad.decompose()    # rip it out
		
	for ad in soup('div', {'id': 'story-ad--aggro-10'}):
		ad.decompose()    # rip it out
		
	for ad in soup('div', {'id': 'story-ad--aggro-12'}):
		ad.decompose()    # rip it out

	for ad in soup('div', {'id': 'story-ad--aggro-14'}):
		ad.decompose()    # rip it out
		
	for ad in soup('div', {'id': 'story-ad--aggro-16'}):
		ad.decompose()    # rip it out
	
	for a in soup('a', {'class': 'visually-hidden skip-to-text-link'}):
		a.decompose()    # rip it out

	for a in soup('a', {'class': 'feedback-link'}):
		a.decompose()    # rip it out

	
	
	# kill all script and style elements
	for script in soup(['script', 'header', 'nav', 'span', 'title', 'li', 'script', 'style', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'button', 'em', 'meta', 'img', 'time', 'form', 'section', 'figure', 'footer']):
		script.decompose()    # rip it out
	
	#print(soup)
	'''
	#text = strip_tags(str(soup), ['div', 'p', 'a'])
	lst = []
	for p in soup.find_all('p'):
		p = p.contents
		''if len(p) > 1:
			for ele in p:
				if ele is NavigableString:
					ele = str(ele)	#convert it from unicode to regular string
			p = ''.join(p)
		else:
			p = p[0]''
		p = p[0]
		#print(p)
		#p.strip()
		''if p.contents: #if there is an <a></a> tag inside <p> </p>
			a = strip_tags(str(p.a), ['a'])''
		p = p.encode('ascii', 'ignore')
		#print(p)
		#p = ''.join(lst)
		if "</a>" in p:
			p = strip_tags(p, ['a'])
			p = str(p)
			p = p[0]
			lst.append(repr(p))
			continue
		
		#p = ''.join(lst)
		#print (lst)
		lst.append(p)
		
		#lst.append('<br/>')

	print (lst)
	'''
	# get text
	text = soup.get_text()
	text = text.strip()
	
	#print(lst)
	return headline, text
	
def strip_tags(html, invalid_tags):
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.find_all(True):
        if tag.name in invalid_tags:
            s = ""

            for c in tag.contents:
                if not isinstance(c, NavigableString):
                    c = strip_tags(unicode(c), invalid_tags)
                s += unicode(c)

            tag.replace_with(s)

    return soup
	
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