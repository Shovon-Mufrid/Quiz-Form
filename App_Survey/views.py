# views.py

from django.shortcuts import render, redirect
from .models import CanteenStaticSurvey
from .forms import CanteenSurveyForm

def canteen_survey(request):
    if request.method == 'POST':
        form = CanteenSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('App_Survey:thank_you')
    else:
        form = CanteenSurveyForm()

    return render(request, 'App_Survey/canteen_survey.html', {'form': form})

def thank_you(request):
    return render(request, 'App_Survey/thank_you.html')
