from django.forms import ModelForm, CharField, ValidationError
from myapp.models import Entry

class EmptyField(CharField):
	def clean(self, value):
		if value!='':
			raise ValidationError('Please DO NOT fill this field!')
class EntryForm(ModelForm):
	do_not_use=EmptyField(label="Do not fill")
	def __init__(self, data=None, *args, **kwargs):
		if data=={}:
			data=None
		ModelForm.__init__(self, data, *args, **kwargs)
	class Meta:
		model=Entry
