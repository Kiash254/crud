import imp
from pyexpat import model
from attr import field
from django.forms import ModelForm
from .models import Port

class PortForm(ModelForm):
    class Meta:
        model=Port
        fields="__all__"
     