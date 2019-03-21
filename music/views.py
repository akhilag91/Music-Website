# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import AddSongForm

from django.conf import settings
from django.http import Http404,HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    albums = Album.objects.all()
    print(albums)
    return render(request,'home.html',{'albums':albums})

def album_detail(request,id):
    album = get_object_or_404(Album,id = id)
    context = {'album' : album}
    songs = Song.objects.filter(album = id)
    playlists = Playlist.objects.all()
    # for song in songs:
    #     print(song.__dict__)
    context.update({'songs' : songs,'playlists': playlists })
    
    return render(request,'album_detail.html',context)

def profile(request):
    return render(request,'profile.html')

def song_upload_form(request):
    if request.method =='POST':
        form = AddSongForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddSongForm()
    return render(request,'song_upload_form.html',{'form':form})

""" creation of playlists """

def crud_playlist(request):
    user = request.user
    print("in view")
    if request.method == 'POST':
        print("in post")
        Playlist.objects.create(
                name = request.POST.get('name'),
                user = user,
                )
    
    playlists = Playlist.objects.filter(user=user.id)
    
    """ playlist_songs = []
    
    for playlist in playlists:
        songs = PlaylistSongs.objects.filter(playlist_id=playlist.id)
        playlist_songs.append(songs) """
        
    """ 'playlist_songs':playlist_songs,- was added to context dic along wid code commented above """
    
    context = {
        'playlists': playlists,
        
        }
    return render(request,'playlist.html',context)
 
""" save songs in playlist """

@csrf_exempt
def save_playlist(request):
    songId = request.POST.get('songId')
    playListId = request.POST.get('playlistId')
    PlaylistSongs.objects.create(
        playlist_id = int(playListId),
        song_id = int(songId) 
    )
    return HttpResponse('success')

""" for viewing playlist songs. songs will be displayed based on playlist id """

""" def view_playlist(request,id):
    playlists = Playlist.objects.all()
    playlistsongs = PlaylistSongs.objects.filter(playlist=id)
    return render(request,'playlistsongs.html',{'playlistsongs' : playlistsongs,'playlists':playlists})
 """
def view_playlist(request,id):
    playlists = Playlist.objects.all()
    playlistsongs = PlaylistSongs.objects.filter(playlist=id)
    return render(request,'playlistsongs.html',{'playlistsongs' : playlistsongs,'playlists':playlists})




    


