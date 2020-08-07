from django import forms
from .models import Job, Spell, Server, Slot, Ability, Equipment, Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character 
        fields = ['id']

class LoadoutForm(forms.Form):  
    weapon = forms.CharField(label='Weapon', max_length=100)
    sub = forms.CharField(label='Sub', max_length=100)