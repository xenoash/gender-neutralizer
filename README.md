# gender-neutralizer
Gender Neutralizer is a web service and RESTful API that simply converts gender-specific text into gender-neutral text. It was tested on Google App Engine (GAE) standard enviornment on the cloud with Python 2.7, django non-rel for the NoSQL Google Datastore implementation.

The tool is mashed up with NYT search API to look for NYT articles to convert their text into geneder-neutral text. However, the built-in neutralize function of the tool can basically work with any url that we insert in the url as in the following URL pattern: 

/view/[put url that starts with http://]/

The tool also provides a RESTful API functionality by taking user input from the url to generate JSON data that includes the user input, generated gender-neutral output, gender-specific words, and their respective equivalent gender-neutral words.

Inserting user input can be done using the following URL patterns after the domain name, to receive html or JSON-formatted data respectively: 
 
 /view/[put userInput here with spaces]

 /view/[put userInput here with spaces]/json

Additionally, the service allows to upload text documents to convert their text into gender-neutral form.
