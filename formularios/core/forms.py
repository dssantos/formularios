from django import forms


class UploadForm(forms.Form):
    upload = forms.FileField()


class OptionsForm(forms.Form):
    options = (('Não','Não'), ('Sim','Sim'))
    indicacao = forms.ChoiceField(choices=options)