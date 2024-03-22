from django import forms
from .models import Book
from captcha.fields import CaptchaField
from captcha.helpers import math_challenge


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
class SearchForm(forms.Form):
    title = forms.CharField(max_length = 255)
    captcha = CaptchaField(generator = 'captcha.helpers.math_challenge')

    