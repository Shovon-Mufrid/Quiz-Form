from django.urls import path
from . import views

app_name = 'App_Survey'

urlpatterns = [
    path('', views.canteen_survey, name='canteen_survey'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
