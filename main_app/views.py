from django.shortcuts import render,redirect
from .forms import WackyWidgetForm
from .models import WackyWidget
from django.views.generic.edit import CreateView





# Create your views here.
def index(request):
    widget_form = WackyWidgetForm()
    total_quantity = 0
    all_widgets = WackyWidget.objects.all()
    for widget in all_widgets:
        total_quantity += widget.quantity
    return render(request, 'index.html', {
        'wacky_form': widget_form,
        'widget_list': all_widgets,
        'total_quantity': total_quantity 
        })



class WidgetCreate(CreateView):
    model = WackyWidget
    fields = ['description', 'quantity']
    success_url = '/'

def DeleteWidget(request, pk):
  widget = WackyWidget.objects.get(id=pk)
  widget.delete()
  return redirect('index')

