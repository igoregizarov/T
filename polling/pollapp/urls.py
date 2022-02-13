from django.urls import path
import pollapp.views as pollapp

app_name = 'pollapp'

urlpatterns = [
    path('poll/', pollapp.poll, name='poll'),
    path('quest/', pollapp.quest, name='quest'),
]


