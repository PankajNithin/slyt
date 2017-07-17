from django import forms
from .models import Shortener

class PostURL(forms.ModelForm):
	class Meta:
		model = Shortener
		fields = ('original_url','custom_tag',)