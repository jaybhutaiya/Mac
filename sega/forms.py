from django import forms
from.import models

class leaveform(forms.ModelForm):
    class Meta:
        model=models.leave
        fields='__all__'