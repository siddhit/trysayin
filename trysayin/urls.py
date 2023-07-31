from django.urls import path
from trysayin import views

urlpatterns = [
    path('', views.index, name='index'),
    # Add other URL patterns for your app's views here
]
