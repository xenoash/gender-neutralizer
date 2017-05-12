# gender-neutralizer
A web service and a RESTful API that converts gender-specific text into gender-neutral text. It has run and was tested on the Google App Engine (GAE) on the cloud 

The tool is mashed up with NYT search API to look for NYT articles to convert their text into geneder-neutral text.

The tool also provides a RESTful API functionality by taking user input from the url to generate JSON data that includes the user input, generated gender-neutral output, gender-specific words, and their respective equivalent gender-neutral words.

Inserting user input can be done using the following URL patterns after the domain name, to receive html or JSON-formatted data respectively: 
/view/<userInput>
/view/<userInput>/json

Additionally, the service allows to upload text documents to convert their text into gender-neutral form.
