from django import forms
from main.models import Prefer

class PreferForm(forms.ModelForm):
    # Meta의 의미를 모르겠군여
    class Meta:
        model = Prefer
        fields = ('prefer_title', 'prefer_content')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prefer_title'].label = "제목"
        self.fields['prefer_content'].label = "내용"
        self.fields['prefer_title'].widget.attrs.update({
            # 클래스 이름 바꿔야 해요
            'class': 'prefer_title',
            'placeholder': '제목',
        })
