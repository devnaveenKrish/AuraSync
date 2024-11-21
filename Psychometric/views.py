from django.shortcuts import render, redirect
from .models import psychometric_question, Users_answers
from django.contrib.auth.models import User

def psychometric(request):
    return render(request, 'psychometric/psychometic.html')

# views.py


def psychometric_questions(request):
    if request.method == "POST":
        # Get current user (if authentication is being used, otherwise handle user manually)
        user = request.user

        # Capture answers for each question from the POST request
        q1_answer = request.POST.get("question-1")
        q2_answer = request.POST.get("question-2")
        q3_answer = request.POST.get("question-3")
        q4_answer = request.POST.get("question-4")
        q5_answer = request.POST.get("question-5")
        q6_answer = request.POST.get("question-6")
        q7_answer = request.POST.get("question-7")
        q8_answer = request.POST.get("question-8")
        q9_answer = request.POST.get("question-9")
        q10_answer = request.POST.get("question-10")

        # Save the answers in the Users_answers model
        Users_answers.objects.create(
            User_id=user,
            q1=q1_answer,
            q2=q2_answer,
            q3=q3_answer,
            q4=q4_answer,
            q5=q5_answer,
            q6=q6_answer,
            q7=q7_answer,
            q8=q8_answer,
            q9=q9_answer,
            q10=q10_answer,
            response_status=True  # Or any logic to update response_status if needed
        )

        return redirect('psychometric')  # Redirect to a 'thank you' or results page after submission

    # Fetch all psychometric questions from the database
    questions = psychometric_question.objects.all()

    context = {
        'questions': questions,
    }
    
    return render(request, 'psychometric/psychometric_questions.html', context)
