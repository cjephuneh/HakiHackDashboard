from .models import Govpersonnel
from django.forms import ModelForm

class Reportingform(ModelForm):
    class Meta:
        model = Govpersonnel
        fields = ('image', 'name', 'service_number', 'email', )