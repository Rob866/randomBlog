from django import forms 

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Ingresa tu nombre"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"Email"}))
    to =  forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"Email"}))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Comentario'}))

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Ingresa tu nombre"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"Email"}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Comentario'}))


class SearchForm(forms.Form):
    query =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Busqueda'}))

