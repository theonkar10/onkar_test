from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length = 30)
    is_active = models.BooleanField(default =  True)
    added_on = models.DateTimeField(auto_now_add=True, blank=True)
    quiz_taken = models.IntegerField(default = 0) 
    def __str__(self):
       return self.category_name    

class QuizAnswers(models.Model):
    quiz_answer = models.CharField(max_length = 100)
    is_correct =  models.BooleanField(default = False)
    added_on  = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
      return self.quiz_answer+ " - "+ str(self.is_correct)


class QuizQuestion(models.Model):
    quiz_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question_title = models.CharField(max_length = 200)
    options = models.ManyToManyField(QuizAnswers, related_name='quiz_answers')
    added_on = models.DateTimeField(auto_now_add=True, blank=True)
    updated_on = models.DateTimeField(blank=True)
   
    def __str__(self):
       return self.quiz_category.category_name + " - "+ self.question_title 


class QuizResults(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     correct_score =  models.IntegerField()
     total_qustions = models.IntegerField()
     added_on = models.DateTimeField(auto_now_add=True, blank=True)
     updated_on = models.DateTimeField(blank=True)
