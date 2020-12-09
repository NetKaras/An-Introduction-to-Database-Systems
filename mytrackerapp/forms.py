from django import forms
from .models import RecordModel

class RecordForm(forms.ModelForm):
    class Meta:
        model = RecordModel
        fields = "__all__"