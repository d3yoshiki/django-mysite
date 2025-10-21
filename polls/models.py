from django.db import models


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
