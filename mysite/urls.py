"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from polls import views  # Question一覧用ビューをインポート


urlpatterns = [
    path('admin/', admin.site.urls),
        path('', views.question_list, name='home'),  # ルートURLに Question一覧を表示
   path('polls/', include('polls.urls')),  # pollsアプリのURLを追加
    path('accounts/', include('social_django.urls', namespace='social')),
    path('login/', views.login_view, name='login'),
    path('after_login/', views.after_login, name='after_login'),  
        path('after_login/', views.mypage, name='after_login'),  # マイページ
        path('logout/', views.logout_view, name='logout'),



]
