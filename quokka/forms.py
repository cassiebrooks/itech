from django import forms
from django.contrib.auth.models import User
from quokka.models import Question, Answer, Votes, Set, UserProfile


class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(queryset=Question.objects.all())
    text = forms.CharField(max_length=512)

    class Meta:
        # Provide an association between the ModelForm and a model
        model   = Answer
        fields  = ('text', 'question')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
