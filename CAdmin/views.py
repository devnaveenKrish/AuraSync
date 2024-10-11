from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Psychometric.models import psychometric_question


@login_required(login_url='admin_login')
def admin_index(request):
    return render(request, 'Admin/main/admin_index.html')

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            if user.is_staff:
                login(request, user)
                return redirect(admin_index)
            else:
                return render(request, 'Admin/main/sign-in.html', {'msg' : 'Access denied! You are not authorised to enter this dashboard!'})
        else:
            return render(request, 'Admin/main/sign-in.html', {'msg' : 'Access denied! Maybe try using some magic words. Or double check your password!'})
    return render(request, 'Admin/main/sign-in.html')

def admin_logout(request):
    logout(request)
    return redirect(admin_login)

def psychometric_questions(request):
    page = "Psychometric Questions"
    questions = psychometric_question.objects.filter(question_status = True)
    return render(request, 'Admin/psychometric_test/psychometric_question.html', {'page' : page, 'questions' : questions})

def create_question(request):
    if request.method=="POST":
        question = request.POST.get('question')
        option_1 = request.POST.get('option_1')
        option_2 = request.POST.get('option_2')
        option_3 = request.POST.get('option_3')
        option_4 = request.POST.get('option_4')
        correct = request.POST.get('correct')
        if correct == 'option1':
            correct = 1
        elif correct == 'option2':
            correct = 2
        elif correct == 'option3':
            correct = 3
        elif correct == 'option4':
            correct = 4
        elif correct == 'any':
            correct = 5
        quest = psychometric_question.objects.create(question = question, choice_1 = option_1, choice_2 = option_2, choice_3 = option_3, choice_4 = option_4, correct_answer = correct, question_status = True)
        quest.save()
        return redirect(psychometric_questions)
        
    return render(request, 'Admin/psychometric_test/create_question.html')

def delete_question(request, qn_id):
    qn = psychometric_question.objects.get(id = qn_id)
    qn.question_status = False
    qn.save()
    return redirect(psychometric_questions)

def edit_question(request, qn_id):
    qn = psychometric_question.objects.get(id = qn_id)
    if request.method == "POST":
        qn.question = request.POST.get('question')
        qn.choice_1 = request.POST.get('option_1')
        qn.choice_2 = request.POST.get('option_2')
        qn.choice_3 = request.POST.get('option_3')
        qn.choice_4 = request.POST.get('option_4')
        correct_answers = request.POST.get('correct')
        print(correct_answers)
        if correct_answers == 'option1':
            qn.correct_answer = 1
            print(qn.choice_1)
        elif correct_answers == 'option2':
            qn.correct_answer = 2
            print(qn.choice_2)
        elif correct_answers == 'option3':
            qn.correct_answer = 3
            print(qn.choice_3)
        elif correct_answers == 'option4':
            qn.correct_answer = 4
            print(qn.choice_4)
        elif correct_answers == 'any':
            qn.correct_answer = 5
        qn.save()
        return redirect(psychometric_questions)
    return render(request, 'Admin/psychometric_test/edit_questions.html', {'qn' : qn})



    