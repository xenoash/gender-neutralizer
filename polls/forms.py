from django.forms import ModelForm
from polls.models import GenderFile

class GenderForm(ModelForm):

    class Meta:
        model = GenderFile
        fields = ('word','equivalent')