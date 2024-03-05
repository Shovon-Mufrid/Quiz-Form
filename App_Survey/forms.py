# forms.py

from django import forms
from .models import CanteenStaticSurvey

class CanteenSurveyForm(forms.ModelForm):
    class Meta:
        model = CanteenStaticSurvey
        exclude = ['timestamp']

    def __init__(self, *args, **kwargs):
        super(CanteenSurveyForm, self).__init__(*args, **kwargs)
        self.fields['student_name'].label = "Student Name"
        self.fields['student_id'].label = "Student ID"
        self.fields['food_quality'].label = "How is Food Quality?"
        self.fields['food_quantity'].label = "How is Food Quantity?"
        self.fields['food_pricing'].label = "What do you think of the Pricing?"
        self.fields['canteen_satisfaction'].label = "Your satisfaction with our canteen?"
        self.fields['canteen_environment'].label = "Is the environment you are eating hygienic?"
        self.fields['canteen_usage'].label = "How often do you use the canteen?"
        self.fields['canteen_serial'].label = "Is order serial maintained?"
        self.fields['initial_menu'].label = "Is the Menu Okay?"
        self.fields['preferred_menu'].label = "Is there anything that you think should be on the menu?"
        self.fields['staff_behavior'].label = "How is the Staff Behaviour?"
        self.fields['note'].label = "Any comments on food and service?"


# from django import forms
# from .models import Survey, Question, Choice, Response

# class SurveyForm(forms.Form):
#     # Define the class first
#     review = forms.CharField(widget=forms.Textarea, required=False)  # Review note

#     # Then create the question fields within the loop (ensure proper indentation)
#     for question in Survey.objects.all():
#         if question.question_set.exists():  # Use question.question_set
#             choices = [(choice.id, choice.text) for choice in question.question_set.all()]
#             field = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)
#         else:
#             field = forms.CharField(widget=forms.Textarea)
#         setattr(SurveyForm, f'question_{question.id}', field)
