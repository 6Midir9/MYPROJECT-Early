from django import forms
from .models import Announcement

class AnnounForm(forms.ModelForm):

    class Meta:
        
        model = Announcement
        fields = ['title', 'text', 'price', 'contact_email']