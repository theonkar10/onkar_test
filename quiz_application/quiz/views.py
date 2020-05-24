from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return True


def show_quiz(request,cat_id):
    if request.method == 'GET':
        questions = QuizQuestion.objects.filter(quiz_category__id = cat_id, quiz_category__is_active = True).order_by('added_on')
        return render(request, 'quiz.html',{'count':questions.count(),'questions':questions})
    else:
        login_data = request.POST.dict()
        print(login_data)
#def load_next_question(request,cat_id,question_id):
    
