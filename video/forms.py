from django import forms

from .models import Video

INPUT_CLASS = 'w-full py-4 px-6 rounded-xl border'

class NewVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('video', 'name', 'description', 'type')

        widgets = {
            'video': forms.FileInput(attrs={
                'class': INPUT_CLASS,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
            }),
            'type': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
        }

class EditVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('video', 'name', 'description', 'type')

        widgets = {
            'video': forms.FileInput(attrs={
                'class': INPUT_CLASS,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
            }),
            'type': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
        }