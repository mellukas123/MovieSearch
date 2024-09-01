from django import forms

class MovieSearchForm(forms.Form):
    title = forms.CharField(label='Movie Title', max_length=100)



class BookmarkForm(forms.Form):
    # This form can be expanded if needed
    pass
