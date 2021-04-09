from django.forms import ModelForm
from .models import WackyWidget





class WackyWidgetForm(ModelForm):
  class Meta:
    model = WackyWidget
    fields = ['description', 'quantity']