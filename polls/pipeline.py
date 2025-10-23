from .models import UserProfile

def create_user_profile(backend, user, response, *args, **kwargs):
    """
    OAuthログインでユーザー作成後に自動でUserProfileを作成
    """
    UserProfile.objects.get_or_create(user=user)
