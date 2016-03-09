from django import forms
from quokka.models import Question, Answer, Votes, Set


class AnswerForm(forms.ModelForm):
    text = forms.CharField(max_length=512)
    class Meta:
        # Provide an association between the ModelForm and a model
        model   = Answer
        fields  = ('text',)