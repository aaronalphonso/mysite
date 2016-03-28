from django import forms

class NameForm(forms.Form):
    question_text = forms.CharField(label='Question', max_length=200)
    choice1 = forms.CharField(label='Choice1', max_length=200)
    choice2 = forms.CharField(label='Choice2', max_length=200)
    choice3 = forms.CharField(label='Choice3', max_length=200)
    choice4 = forms.CharField(label='Choice4', max_length=200)
