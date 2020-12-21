from django import forms
from django.core.validators import validate_image_file_extension
from .models import BankFiles


class ShowAdminForm(forms.ModelForm):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label="Add Files",
        required=False,
    )

    class Meta:
        model = BankFiles
        exclude = ("files",)

    def clean_photos(self):
        for upload in self.files.getlist("file"):
            validate_image_file_extension(upload)

    def save_photos(self, show):
        for upload in self.files.getlist("file"):
            files = BankFiles(files=upload)
            files.save()
