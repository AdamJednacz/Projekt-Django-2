from django import forms

from .models import Industry,Offer

class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = '__all__'



class OfferForm(forms.ModelForm):
    name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    mail = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    number = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
    price = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'Price'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Choose a photo'}))
    industry = forms.ModelMultipleChoiceField(queryset=Industry.objects.all())
    text = forms.CharField(max_length=150, widget=forms.Textarea(attrs={'placeholder': 'Description'}))

    class Meta:
        model = Offer
        fields = '__all__'



