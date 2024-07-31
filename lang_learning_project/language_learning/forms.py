from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word_text', 'meaning', 'pronunciation', 'category']
        
class QuizForm(forms.Form):
    answer = forms.CharField(label='정답', max_length=255)