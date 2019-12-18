#playlist/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='Home'),
    path('ask/', views.ask, name='ask'),
    #path('share', views.share, name='share'),
    path('add', views.UrlinkerCreate.as_view(), name='add'),
]
