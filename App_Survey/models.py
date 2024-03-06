# # models.py

# from django.db import models

# class Survey(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()

#     def __str__(self):
#         return self.title

# class Question(models.Model):
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
#     text = models.TextField()
#     answer = models.CharField(max_length=255)

#     def __str__(self):
#         return self.text

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     text = models.CharField(max_length=255)
#     answer = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return f"{self.question.text} --- {self.text}"

# class Response(models.Model):
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
#     student = models.EmailField(max_length=255, null=True, blank=True)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
#     review = models.TextField()

#     def __str__(self):
#         return f"{self.student}'s response to {self.survey.title}"
    
# # class Feedback(models.Model):
# #     student_mail = models.CharField(max_length=255)
# #     food_pricing = models.PositiveIntegerField()
# #     satisfaction = models.PositiveIntegerField()
# #     hygiene_satisfaction = models.BooleanField()
# #     frequency_of_use = models.CharField(max_length=20, choices=[
# #         ('daily', 'Daily'),
# #         ('weekly', 'Weekly'),
# #         ('monthly', 'Monthly'),
# #         ('rarely', 'Rarely'),
# #     ])
    

# class CanteenStaticSurvey(models.Model):
#     student_name = models.CharField(max_length=255, null=True, blank=True)
#     student_id = models.CharField(max_length=255, unique = True)
#     food_quality = models.CharField(max_length=20, choices=[
#         ('best', 'Best'),
#         ('satisfactory', 'Satisfactory'),
#         ('moderate', 'Moderate'),
#         ('worst', 'Worst'),
#     ])
#     food_quantity = models.CharField(max_length=20, null=True, blank=True, choices=[
#         ('best', 'Best'),
#         ('satisfactory', 'Satisfactory'),
#         ('moderate', 'Moderate'),
#         ('worst', 'Worst'),
#     ])
#     food_pricing = models.CharField(max_length=20, null=True, blank=True, choices=[
#         ('best', 'Best'),
#         ('satisfactory', 'Satisfactory'),
#         ('moderate', 'Moderate'),
#         ('worst', 'Worst'),
#     ])
#     canteen_satisfaction = models.CharField(max_length=20, null=True, blank=True, choices=[
#         ('best', 'Best'),
#         ('satisfactory', 'Satisfactory'),
#         ('moderate', 'Moderate'),
#         ('worst', 'Worst'),
#     ])
#     canteen_environment = models.CharField(max_length=20, null=True, blank=True, choices=[
#         ('best', 'Best'),
#         ('satisfactory', 'Satisfactory'),
#         ('moderate', 'Moderate'),
#         ('worst', 'Worst'),
#     ])
#     canteen_usage = models.CharField(max_length=20, null=True, blank=True, choices=[
#         ('daily', 'Daily'),
#         ('occasionally', 'Occasionally'),
#         ('never', 'Never'),
#     ])
#     canteen_serial = models.CharField(max_length=20, null=True, blank=True, choices=[
#         ('best', 'Best'),
#         ('satisfactory', 'Satisfactory'),
#         ('moderate', 'Moderate'),
#         ('worst', 'Worst'),
#     ])
#     initial_menu = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True)
#     preferred_menu = models.CharField(max_length=255, null=True, blank=True)
#     staff_behavior = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True)
#     note = models.TextField(max_length=255, null=True, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.student_id} - {self.timestamp}"


