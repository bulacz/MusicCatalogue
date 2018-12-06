from django.contrib.sessions import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render


# Create your views here.
from django.views import View
from requests import Response

from albumlist.forms import AddArtistForm, AddAlbumForm, BrowseCatalogueForm
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
        return render(request, "../templates/show-albums.html", {'albums': albums, })


class BrowseCatalogue(View):
    def get(self, request):
        form = BrowseCatalogueForm
        artists = Artist.objects.all().order_by('name')
        return render(request, "../templates/browse-catalogue.html", {'form': form})


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
        if 'discogsLink' in request.POST:
            form = AddAlbumForm(request.POST)
            band_id = form.data['band']
            band_to_discogs = Artist.objects.get(pk=band_id).name
            user_agent = 'Bootcamp graduation app - MusicCatalogue by bulacz'
            discogsclient = discogs_client.Client(user_agent, user_token=disocgs_data['app_token'])
            results = discogsclient.search(f'{band_to_discogs}', type='artist', role='main', )
            releases = results[0].releases
            return render(request, 'add-album.html', {"form": form, "releases": releases})

        elif 'addAlbumSubmit' in request.POST:
            form = AddAlbumForm(request.POST)
            print(request.POST)
            Album.objects.create(
                band=Artist.objects.get(pk=int(request.POST['band'][0])),
                title=request.POST['title'],
                release_year=request.POST['release_year'],
                songs=request.POST['songlist'][0],
                type=request.POST['type'],
                location=request.POST['location']
                )
            return HttpResponseRedirect('/albumlist')


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


class ShowAlbumsByArtist(View):
    def get (self, request, artist_id):
        artist = Artist.objects.get(pk=artist_id)
        albums = Album.objects.filter(band=artist)
        # data = serializers.serialize("json", Album.objects.filter(band=artist))
        data_list = list(albums.values())
        print(data_list)
        print(data_list[0])
        print(data_list[1])
        print(len(data_list))

        return JsonResponse(data_list, safe=False)

        # JSONSerializer = serializers.get_serializer("")
        # xml_serializer = XMLSerializer()
        # xml_serializer.serialize(queryset)
        # data = xml_serializer.getvalue()




