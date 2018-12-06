from django import forms


from albumlist.models import Artist, RECORD_TYPES, LOCATIONS, Album


class AddArtistForm(forms.Form):
    name = forms.CharField(max_length=160, label="Nazwa artysty")


class AddAlbumForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AddAlbumForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

    band = forms.ModelChoiceField(queryset=Artist.objects.all().order_by('name'))
    title = forms.CharField(max_length=160, label="Tytuł albumu", required=False)
    release_year = forms.IntegerField(required=False)
    songlist = forms.CharField(max_length=1410, required=False)
    type = forms.ChoiceField(label='nośnik', choices=RECORD_TYPES)
    location = forms.ChoiceField(label='lokalizacja', choices=LOCATIONS)


class BrowseCatalogueForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BrowseCatalogueForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

    browse_band = forms.ModelChoiceField(queryset=Artist.objects.all().order_by('name'))

