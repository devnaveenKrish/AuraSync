from django.db import models
from django.contrib.auth.models import User

class psychometric_question(models.Model):
    question = models.TextField()
    choice_1 = models.CharField(max_length=225)
    choice_2 = models.CharField(max_length=225)
    choice_3 = models.CharField(max_length=225)
    choice_4 = models.CharField(max_length=225)
    correct_answer = models.CharField(max_length=225)
    question_status = models.BooleanField(default=True)

    def __str__(self):
        return f'Question_{self.id}'
    
class Users_answers(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    q1 = models.CharField(max_length=10)
    q2 = models.CharField(max_length=10, null=True)
    q3 = models.CharField(max_length=10, null=True)
    q4 = models.CharField(max_length=10, null=True)
    q5 = models.CharField(max_length=10, null=True)
    q6 = models.CharField(max_length=10, null=True)
    q7 = models.CharField(max_length=10, null=True)
    q8 = models.CharField(max_length=10, null=True)
    q9 = models.CharField(max_length=10, null=True)
    q10 = models.CharField(max_length=10, null=True)
    response_status = models.BooleanField(default=True)


