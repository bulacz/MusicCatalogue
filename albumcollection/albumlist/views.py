from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

# Create your views here.
from django.views import View

from albumlist.forms import AddArtistForm, AddAlbumForm
from albumlist.models import Album, Artist


class ShowMainPage(View):
    def get(self, request):
        return render(request, "main-page.html")

class ShowAlbumList(View):
    def get(self, request):
        albums = Album.objects.all()
        return render(request, "../templates/show-albums.html", {'albums': albums})

class ShowAllArtists(View):
    def get(self, request):
        artists = Artist.objects.all()
        return render(request, "../templates/show-artists.html", {'artists': artists})

class AddArtist(View):
    def get(self, request):
        form = AddArtistForm()
        return render(request, "add-artist.html", {"form": form})

    def post(self, request):
        form = AddArtistForm(request.POST)
        if form.is_valid():
            new_artist = Artist.objects.create(name=form.cleaned_data['name'])
            return HttpResponseRedirect('/artistslist')


class AddAlbum(View):
    def get(self, request):
        form = AddAlbumForm().as_p()
        return render(request, 'add-album.html', {"form": form})


class ShowAlbum(View):
    def get(self, request, album_id):
        album = Album.objects.get(pk=album_id)
        return render(request, "show-single-album.html", {"album": album})

class DeleteAlbum(View):
    def get(self, request, album_id):
        try:
            album = Album.objects.get(pk=album_id)
            album.delete()
            return HttpResponseRedirect('/albumlist')
        except ObjectDoesNotExist:
            return Http404

class DeleteArtist(View):
    def get(self, request, artist_id):
        try:
            artist = Artist.objects.get(pk=artist_id)
            artist.delete()
            return HttpResponseRedirect('/artistslist')
        except ObjectDoesNotExist:
            return Http404


class ShowArtist(View):
    def get(self, request, artist_id):
        artist = Artist.objects.get(pk=artist_id)
        return render (request, "show-single-artist.html", {"artist": artist})