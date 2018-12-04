from django.shortcuts import render

# Create your views here.
from django.views import View

from albumlist.models import Album, Artist


class ShowAlbumList(View):
    def get(self, request):
        albums = Album.objects.all()
        return render(request, "../templates/show-albums.html", {'albums': albums})

class ShowAllArtists(View):
    def get(self, request):
        artists = Artist.objects.all()
        return render(request, "../templates/show-artists.html", {'artists': artists})
