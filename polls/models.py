from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Question(models.Model):
    title = models.CharField(max_length=200)  # 質問のタイトル（例：「消費税を引き下げるべきか？」）
    description = models.TextField(blank=True)  # 詳しい説明や背景
    pub_date = models.DateTimeField(auto_now_add=True)  # 投稿日

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=100)  # 選択肢のテキスト（例：「賛成」「反対」「わからない」）
    votes = models.IntegerField(default=0)  # 投票数

    def __str__(self):
        return f"{self.text} ({self.votes}票)"





class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', '男性'),
        ('female', '女性'),
        ('other', 'その他'),
    ]

    PARTY_CHOICES = [
        ('none', '支持政党なし'),
        ('liberal', '自由民主党'),
        ('ishin', '維新の会'),
        ('kyosan', '共産党'),
         ('rikken', '立憲民主党'),
        ('kokumin', '国民民主党'),
        ('other', 'その他の党'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField("ユーザネーム", max_length=50)
    profile_comment = models.TextField("プロフィールコメント", blank=True)
    gender = models.CharField("性別", max_length=10, choices=GENDER_CHOICES, blank=True)
    birth_year = models.IntegerField("生まれた年", null=True, blank=True)
    registered_at = models.DateTimeField("登録日", default=timezone.now)
    political_party = models.CharField("支持政党", max_length=20, choices=PARTY_CHOICES, blank=True)

    def __str__(self):
        return self.nickname or self.user.username
