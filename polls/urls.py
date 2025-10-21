from django.urls import path
from . import views

urlpatterns = [
        path('', views.question_list, name='question_list'),        # 一覧
    path('create/', views.create_question, name='create_question'),

]
