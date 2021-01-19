from django import forms

class NewEntryPageForm(forms.Form):
    entryTitle = forms.CharField(
        label='Title of New Entry Page:', 
        max_length=30,
        required=True
    )
    entryContent = forms.CharField(
        label='Add content here:', 
        max_length=200,
        widget=forms.Textarea(attrs={'rows': 2, 'cols': 120, 'style': 'height: 5em;'}),
        required=True
    )

class EditEntryPageForm(forms.Form):
    entryContent = forms.CharField(
        label='Edit content here:', 
        max_length=1000,
        widget=forms.Textarea(attrs={'rows': 2, 'cols': 120, 'style': 'height: 5em;'})
    )