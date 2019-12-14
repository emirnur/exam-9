from django.forms import ModelForm

from webapp.models import Photo


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'sign']