# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import User
import datetime
from django.db import models

    
class Album(models.Model):
    album_name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

    def __str__(self):
        return self.album_name + " - " + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    file_type = models.FileField(upload_to='songs')
    
    def __str__(self):
        return self.song_title

class Playlist(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

class PlaylistSongs(models.Model):
    playlist = models.ForeignKey(Playlist)
    song = models.ForeignKey(Song)
    deleted = models.BooleanField(default=False)

