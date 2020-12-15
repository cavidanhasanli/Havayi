from django import forms
from django.core.validators import validate_image_file_extension
from .models import BankFiles


class ShowAdminForm(forms.ModelForm):
    class Meta:
        model = BankFiles
        exclude = ("files",)

    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label="Add Files",
        required=False,
    )

    def clean_photos(self):

        for upload in self.files.getlist("file"):
            validate_image_file_extension(upload)

    def save_photos(self, show):

        for upload in self.files.getlist("file"):
            photo = BankFiles(files=upload)
            photo.save()