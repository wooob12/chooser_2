from django import forms
from main.models import Debate, Comment_debate


class DebateForm(Forms.ModelForm):
    class Meta:
        model = Debate
        fields = ('debate_img1', 'debate_img2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['debate_img1'].label = "사진1"
        self.fields['debate_img2'].label = "사진2"
        self.fields['debate_img1_name1'].label = "사진이름1"
        self.fileds['debate_img2_name2'].label = "사진이름2"




class DebateCommentForm(forms.ModelForm):

    class Meta:
        model = Comment_prefer
        fields = ('com_pre_content' )