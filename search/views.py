from django.shortcuts import render
from search.nyt import callfunc
import requests

	
def search(request):
	result_list = []
	page_number = 0
	query = ''
	if request.method == 'POST':
		query = request.POST['query'].strip()
		page_number = request.POST['page_number']
		if query:
			result_list = callfunc(query, page_number)
	return render(request, 'search/search.html', {
			'result_list': result_list,
			'page_number' : page_number, 
			'query' : query
		})