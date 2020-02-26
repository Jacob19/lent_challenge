from django import forms
from .models import Tasks


#Form for the Tasks list
class TasksList(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
