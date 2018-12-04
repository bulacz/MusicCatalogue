from django import forms

from albumlist.models import Artist, RECORD_TYPES, LOCATIONS, Album


class AddArtistForm(forms.Form):
    name = forms.CharField(max_length=160, label="Nazwa artysty")


# class AddAlbumForm(forms.Form):
#     # band = forms.ChoiceField(choices=ARTISTS)
#     band = forms.Fo
#     title = forms.CharField(max_length=160, label="Tytuł albumu")
#     release_year = forms.IntegerField()
#     songslist = forms.Textarea()
#     type = forms.ChoiceField(label='nośnik', choices=RECORD_TYPES)
#     location = forms.ChoiceField(label='lokalizacja', choices=LOCATIONS)

class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

