from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

# Create your views here.
from django.views import View

from albumlist.forms import AddArtistForm, AddAlbumForm
from albumlist.models import Album, Artist

import sys
import discogs_client
from discogs_client.exceptions import HTTPError

try:
    from albumcollection.discogsAuth import disocgs_data
except ModuleNotFoundError:
    print("Uzupełnij dane i spróbuj ponownie!")
    exit(0)


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
        bands = Artist.objects.all().order_by('name')
        form = AddAlbumForm().as_p()
        return render(request, 'add-album.html', {"form": form})

    def post(self, request):
        print(request.POST)
        if 'discogsLink' in request.POST:
            print("1")
            form = AddAlbumForm(request.POST)
            print("2")
            band_id = form.data['band']
            print("3")
            band_to_discogs = Artist.objects.get(pk=band_id).name
            print("4")
            user_agent = 'Bootcamp graduation app - MusicCatalogue by bulacz'
            print("5")
            discogsclient = discogs_client.Client(user_agent, user_token=disocgs_data['app_token'])
            print("6")
            results = discogsclient.search(f'{band_to_discogs}', type='artist', role='main', )
            print("7")
            releases = results[0].releases
            print("releases", releases)
            return render(request, 'add-album.html', {"form": form, "releases": releases})




        #
        # form = AddAlbumForm(request.POST)
        # band_id = form.data['band']
        # band_to_discogs = Artist.objects.get(pk=band_id).name
        # print("Wychodzi", band_to_discogs)
        #
        # ## realizacja zapytania do API,
        # ## przygotowanie klienta:
        # user_agent = 'Bootcamp graduation app - MusicCatalogue by bulacz'
        #
        # ## przekazanie tokena aplikacji. Aplikacja nie podszywa się pod dowolnego zalogowanego w niej użytkownika
        # discogsclient = discogs_client.Client(user_agent, user_token=disocgs_data['app_token'])
        #
        # '''
        # ##przekazanie klientowi danych niezbędnych do walidacji
        # discogsclient.set_consumer_key(disocgs_data['consumer_key'], disocgs_data['consumer_secret'])
        # discogsclient.get_authorize_url(disocgs_data['request-token'], "request-secret", disocgs_data['authorize-url'])
        #
        # # token, secret, url = discogsclient.get_authorize_url()
        # try:
        #     access_token, access_secret = discogsclient.get_access_token(oauth_verifier)
        # except HTTPError:
        #     print
        #     'Unable to authenticate.'
        #     sys.exit(1)
        #
        # '''
        #
        # results = discogsclient.search(f'{band_to_discogs}', type='artist', role='main', )
        # releases = results[0].releases
        #
        #
        # # print("Przychodzi", results[0].name)
        # # print("Przychodzi", results[0].id)
        # #
        # # for each_release in results[0].releases:
        # #     print(each_release.title, ":", each_release.tracklist)
        # #     # print(each_release.data['title'], each_release.data['tracklist'])
        # # albums_results = discogsclient.search(artist=results[0].id)
        #
        # return render(request, 'add-album.html', {"form": form})

    # form = AddAlbumForm(request.POST)
    # band_id = form.data['band']
    # band_to_discogs = Artist.objects.get(pk=band_id).name
    # print("Wychodzi", band_to_discogs)




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
        return render(request, "show-single-artist.html", {"artist": artist})
