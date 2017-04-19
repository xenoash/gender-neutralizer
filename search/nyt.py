import json
import requests
#from pprint import pprint
import urllib
from nytimesarticle import articleAPI

api_key = '2a097774894146b281cf8ac2a3528f02'


def callfunc(query, page_number):
	url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q="+ query +"&sort=newest&page="+ page_number +"&api-key="+ api_key

	resp = requests.get(url)
	data = json.loads(resp.text)
	articles = parse_articles(data)
	return articles
	
def parse_articles(articles):
	results = []
	for key in articles['response']['docs']:
		results.append({'headline': key['headline']['main'], 'link': key['web_url'], 'snippet': key['snippet'] })
	return results

	
