from django.shortcuts import render, redirect
from .forms import QuestionForm
from .models import Question

def question_list(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'polls/question_list.html', {'questions': questions})


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list')  # 保存後に一覧ページにリダイレクト
    else:
        form = QuestionForm()
    return render(request, 'polls/create_question.html', {'form': form})
