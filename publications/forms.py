from django import forms
from publications.models import Publication, Comments
from django.forms.widgets import Textarea


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['image', 'description']
        labels = {'image': 'Image', 'description': 'Description'}


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
    
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
        labels = {'text': ''}
        widgets = {
            'text': Textarea(attrs={
                'rows': 4,
                'cols': 50,
                'placeholder': 'Добавьте комментарий',
                'class': 'border-0 border-top',
                'style': 'padding-right: 150px; outline:0px none transparent; overflow:auto; resize:none',
            })
        }