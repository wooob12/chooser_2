from django.db import models

# Create your models here.
# 회원
class Member(models.Model):
    member_id = models.AutoField(primary_key = True)
    member_email = models.CharField(max_length = 30)
    member_pwd = models.CharField(max_length = 20)
    member_nick= models.CharField(max_length = 15)
    member_op = models.BooleanField(default = False)
    member_ban = models.BooleanField(default = False)

    def __str__(self):
        return self.member_nick


# 취향 페이지

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)# PK
    topic_content = models.TextField()
    topic_start_date = models.DateTimeField(auto_now_add=True)
    topic_end_date = models.DateTimeField()



class Prefer(models.Model):
    prefer_id = models.AutoField(primary_key=True) # PK
    prefer_topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # FK
    prefer_member_id = models.ForeignKey(Member, on_delete=models.CASCADE) # FK
    prefer_title = models.CharField(max_length=50)
    prefer_date = models.DateTimeField(auto_now_add=True) # 수정해도 날짜가 안바뀜
    prefer_content = models.TextField()
   # prefer_file = # models.FileField()



class Comment_prefer(models.Model):
    com_pre_id = models.AutoField(primary_key=True) # PK
    com_pre_member_id = models.ForeignKey(Member, on_delete=models.CASCADE) # FK(member_id)
    com_pre_prefer_id = models.ForeignKey(Prefer, on_delete=models.CASCADE) # FK(prefer_id)
    com_pre_content = models.TextField()


# 토론 페이지
class Debate(models.Model):
    debate_id = models.AutoField(primary_key=True) # PK
    debate_pre_date = models.DateTimeField(auto_now_add=True) # 수정해도 날짜가 안바뀜
    debate_img1 = models.ImageField(blank=True)
    debate_img2 = models.ImageField(blank=True)
    debate_img1_name1 = models.CharField(max_length=20)
    debate_img2_name2 = models.CharField(max_length=20)

class Comment_debate(models.Model):
    com_deb_id = models.AutoField(primary_key=True) # PK
    com_deb_member_id = models.ForeignKey(Member, on_delete=models.CASCADE) # FK(member_id)
    com_deb_content = models.ForeignKey(Debate, on_delete=models.CASCADE) # FK(debate_id)
    con_deb_date = models.DateTimeField(auto_now_add=True) # 수정해도 날짜가 안바뀜

class Vote(models.Model):
    vote_id = models.AutoField(primary_key=True) # PK
    vote_member_id = models.ForeignKey(Member, on_delete=models.CASCADE)# FK(member_id)
    vote_debate_id = models.ForeignKey(Debate, on_delete=models.CASCADE)# FK(debate_id)
    vote_result_1 = models.IntegerField()# BooleanField(참거짓)으로 구분할 수 있을까? 언제든지 취소 수정 가능?
    vote_result_2 = models.IntegerField()




# author = models.ForeignKey(User, on_delete=models.CASCADE)

# 날짜 모델 변경
# 투표 결과 정수형으로 한 거 모델 한글에 써놓기
# 모델에 있는 주석들 다 보기