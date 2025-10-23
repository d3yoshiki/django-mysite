from django import forms
from .models import Question,UserProfile

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


YEAR_CHOICES = [(year, str(year)) for year in range(1900, 2026)]



class UserProfileForm(forms.ModelForm):
    birth_year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        label="生まれた年",
        required=False,
        initial=1990  # ← デフォルト値
    )

    class Meta:
        model = UserProfile
        fields = ['nickname', 'profile_comment', 'gender', 'birth_year', 'political_party']
        widgets = {
            'profile_comment': forms.Textarea(attrs={'rows': 3}),
        }