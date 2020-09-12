from django import forms
from main.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('member_email', 'member_pwd', 'member_nick',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['member_email'].label = "EMAIL"
        self.fields['member_pwd'].label = "PASSWARD"
        self.fields['member_nick'].label = "NICKNAME"
