from django import forms
from .models import Prefer

class Prefer(forms.PreferForm):
    # Meta의 의미를 모르겠군여
    class Meta:
        models = Prefer
        fields = ('prefer_title', 'prefer_content')
    
    # *args, **kwargs 의미는 까먹었지만 적었습니다
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prefer_title'].label = "제목"
        self.fields['prefer_content'].label = "내용"
        self.fields['prefer_title'].widget.attrs.update({
            # 클래스 이름 바꿔야 해요
            'class': 'prefer_title',
            'placeholder': '제목',
        })
