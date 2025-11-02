from django.urls import path
from . import views

urlpatterns = [
    
        path('', views.question_list, name='question_list'),        # 一覧
        path('create/', views.create_question, name='create_question'),
        path('edit_profile/', views.edit_profile, name='edit_profile'),
        path('after_login/', views.after_login, name='after_login'),
        path('after_login/', views.mypage, name='after_login'),  # マイページ
    path('mypage/', views.mypage, name='mypage'),  # 新しいマイページURL
    path('question/<int:pk>/', views.question_detail, name='question_detail'),

]
