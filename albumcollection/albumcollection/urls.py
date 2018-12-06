"""albumcollection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

from albumcollection import settings
from albumlist.views import ShowAlbumList, ShowAllArtists, AddArtist, AddAlbum, ShowAlbum, ShowArtist, DeleteAlbum, \
    DeleteArtist, ShowMainPage, BrowseCatalogue, ShowAlbumsByArtist

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^main/$', ShowMainPage.as_view()),
    re_path(r'^albumlist/$', ShowAlbumList.as_view()),
    re_path(r'^artistslist/$', ShowAllArtists.as_view()),
    re_path(r'^add-artist/$', AddArtist.as_view()),
    re_path(r'^add-album$', AddAlbum.as_view()),
    re_path(r'^show-album/(?P<album_id>[0-9]+)$', ShowAlbum.as_view()),
    re_path(r'^show-artist/(?P<artist_id>[0-9]+)$', ShowArtist.as_view()),
    re_path(r'^delete-album/(?P<album_id>[0-9]+)$', DeleteAlbum.as_view()),
    re_path(r'^delete-artist/(?P<artist_id>[0-9]+)$', DeleteArtist.as_view()),
    re_path(r'^browse-catalogue$', BrowseCatalogue.as_view()),
    re_path(r'^show-albums-by-artist/(?P<artist_id>[0-9]+)$', ShowAlbumsByArtist.as_view()),

]

# urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
#     # static files (images, css, javasript, etc.)
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }), ]