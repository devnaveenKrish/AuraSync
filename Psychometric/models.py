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
    q2 = models.CharField(max_length=10)
    q3 = models.CharField(max_length=10)
    q4 = models.CharField(max_length=10)
    q5 = models.CharField(max_length=10)
    q6 = models.CharField(max_length=10)
    q7 = models.CharField(max_length=10)
    q8 = models.CharField(max_length=10)
    q9 = models.CharField(max_length=10)
    q10 = models.CharField(max_length=10)
    response_status = models.BooleanField(default=True)

    def __str__(self):
        return self.User_id


