from django import forms
from .models import Album,Song,Playlist


class AddSongForm(forms.ModelForm):
    class Meta:
        model = Song 
        fields= ('album','song_title','file_type')