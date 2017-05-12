# gender-neutralizer
Gender Neutralizer is a NoSQL web service and RESTful API that simply converts gender-specific text into gender-neutral text. It was tested on Google App Engine (GAE) standard enviornment on the cloud with Python 2.7 and django non-rel package for the NoSQL Google Datastore implementation.

The tool is mashed up with NYT search API to look for NYT articles to convert their text into geneder-neutral text. However, the built-in neutralize function of the tool can basically work with any url that we insert in the url as in the following URL pattern: 

```/view/[put url that starts with http://]/```

The tool also provides a RESTful API functionality by taking user input from the url to generate JSON data that includes the user input, generated gender-neutral output, gender-specific words, and their respective equivalent gender-neutral words.

Inserting user input can be done using the following URL patterns after the domain name, to receive html or JSON-formatted data respectively: 
 
 ```/view/[put userInput here with spaces]```

```/view/[put userInput here with spaces]/json```

Additionally, the service allows to upload text documents to convert their text into gender-neutral form.

### **Implementation:**
The main app contains the following functions which implements the main functionality of the web service.

extract function: This function basically extracts the text of any NYT article chosen by the user or the file content in the case of an uploaded file . To extract the text from NYT articles, we used a python package called Beautiful soup. First, we collect the html content of the page of the article by requesting the URL of the page.

```python
soup = BeautifulSoup(html, 'html.parser')
```

Next, we decompose any returned tags that we do not need such as header, footer, advertisements, and scripts.
```python
for tag in soup(['script', 'header', 'nav', 'span' ...):
tag.decompose()  
```
Afterwards, we will be left with the `<p>` and `<a>` html tags that contain the contents of the article from which we extract the raw text by the get_text() function of the beautiful soup package..

```python
text = soup.get_text()
```

neutralize function: This function contains our main algorithm for the project. Our inability to find a suitable Natural Language processing (NLP) API to help in identifying the gender of words prompted us (after some research) to build our own dictionary of gender-specific words and their gender-neutral equivalents. The algorithm is designed to use this dictionary (note that this dictionary can always be modified by updating or deleting its entries) stored in google cloud datastore to gender neutralize any text. We access the NoSQL database with this code snippet

```python
entries = GenderFile.objects.values()
	gender_to_neutral = {}
	for entry in entries:
		key = entry['word']
		value = entry['equivalent']
		gender_to_neutral[key] = value
```
Once we have this dictionary, we then neutralize the text chosen from NYT or uploaded by the user

```python
ntext = replace_all(text, gender_to_neutral)
```
