from django.db import models

# Create your models here.

class Prefer(models.Model):
    prefer_id = models.AutoField(primary_key=True) # PK
    prefer_topic = models.AutoField(max_length=50) # FK
    prefer_member_id = models.AutoField() # FK
    prefer_title = models.CharField(max_length=50)
    prefer_date = models.DateTimeField(auto_now=True)
    prefer_content = models.TextField()
    prefer_file = 

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)# PK
    topic_content = 
    topic_start_date = 
    topic_end_date = 

class Comment_prefer(models.Model):
    com_pre_id = models.AutoField(primary_key=True) # PK
    com_pre_member_id = # FK(member_id)
    com_pre_prefer_id = # FK(prefer_id)
    com_pre_content = 

class Debate(models.Model):
    debate_id = models.AutoField(primary_key=Auto) # PK
    debate_pre_date =
    debate_img1 =
    debate_img2 =
    debate_img1_name1 =
    debate_img2_name2 =

class Comment_dabate(models.Model):
    com_deb_id = models.AutoField(primary_key=Auto) # PK
    com_deb_member_id = # FK(member_id)
    com_deb_content = # FK(debate_id)
    con_deb_date = 

class Vote(models.model):
    vote_id = models.AutoField(primary_key=Auto) # PK
    vote_member_id = # FK(member_id)
    vote_debate_id = # FK(debate_id)
    vote_result = 




# author = models.ForeignKey(User, on_delete=models.CASCADE)