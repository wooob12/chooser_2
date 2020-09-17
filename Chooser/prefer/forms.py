from django import forms
from main.models import Prefer, Comment_prefer

class PreferForm(forms.ModelForm):
    class Meta:
        model = Prefer
        fields = ('prefer_title', 'prefer_content',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prefer_title'].label = "제목"
        self.fields['prefer_content'].label = "내용"
        self.fields['prefer_title'].widget.attrs.update({
            # 클래스 이름 바꿔야 해요
            'class': 'prefer_title',
            'placeholder': '제목',
        })
        # 날짜 자동 생성
        # self.fields['content'].wedget.attrs.update({
        #     'class': 'prefer_content_form',
        # })

# 댓글 기능
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment_prefer
        fields = ('com_pre_content', )