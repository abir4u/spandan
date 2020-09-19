from django import forms
from amazon.models import News
from ckeditor.fields import RichTextField
class News_Post(forms.ModelForm):
    
    class Meta:
        model = News
        fields = ['title','body','author']
