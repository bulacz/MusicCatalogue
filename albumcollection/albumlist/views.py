from django.shortcuts import render

# Create your views here.
from django.views import View

from albumlist.models import Album


class ShowAlbumList(View):
    def get(self, request):
        albums = Album.objects.all()
        return render(request, "../templates/show-albums.html", {'albums': albums})

