from django import forms
from .models import Topic

# This is a ModelForm associated with the Topic model. The subject in the fields list inside the Meta class is referring to the subject field in the Topic class.
class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        # Communicate that this form is associated with the Topic model
        model = Topic
        fields = ['subject', 'message']