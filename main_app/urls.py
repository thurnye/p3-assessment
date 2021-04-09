from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wackywidget/create/', views.WidgetCreate.as_view(), name='widgets_create'),
    path('wackywidget/<int:pk>/delete', views.DeleteWidget, name='delete'),
   

]