from django.shortcuts import render, redirect,get_object_or_404
from .forms import QuestionForm,UserProfileForm
from .models import Question,UserProfile
from django.contrib.auth.decorators import login_required


def question_list(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'polls/question_list.html', {'questions': questions})


# 質問詳細
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/question_detail.html', {'question': question})


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list')  # 保存後に一覧ページにリダイレクト
    else:
        form = QuestionForm()
    return render(request, 'polls/create_question.html', {'form': form})





def login_view(request):
    return render(request, 'polls/login.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')  # ログアウト後にホームへリダイレクト


@login_required
def edit_profile(request):
    # 初回ログインでまだUserProfileがない場合は作成
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # 保存後はホームへ
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'polls/edit_profile.html', {'form': form})

@login_required
def after_login(request):
    """
    OAuthログイン後のリダイレクト先
    初回ログインなら edit_profile へ、それ以降は home へ
    """
    profile = request.user.userprofile
    # まだ nickname が空なら初回とみなす
    if not profile.nickname:
        return redirect('edit_profile')
    return redirect('home')

@login_required
def mypage(request):
    # ログインユーザーのプロフィールを取得
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'polls/mypage.html', {'profile': profile})