from django import forms
from main.models import Person

class CreateNewPerson(forms.Form):
    first_name = forms.CharField(label="First name",max_length=40)
    last_name = forms.CharField(label="Last name",max_length=40)
    
class AddSubjectToPerson(forms.Form):
   
    subject = forms.CharField(label="Log topic",max_length=30)
    reason = forms.CharField(label="Description",max_length=200)
    
    