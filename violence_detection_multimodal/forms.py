from django import forms
from django.forms import ModelForm
from .models import Video,Audio

class VideoForm(ModelForm):
    class Meta:
    	model= Video
    	fields= ["videofile"]

class AudioForm(ModelForm):
    class Meta:
        model= Audio
        fields= ["text", "audiofile"]



