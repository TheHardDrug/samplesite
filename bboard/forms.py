from django.forms import ModelForm

from .models import Bb


class Bbform(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')
