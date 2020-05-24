from django.contrib import admin
from .models import Category,QuizAnswers,QuizQuestion

# Register your models here.

admin.site.register(Category)
admin.site.register(QuizAnswers)
admin.site.register(QuizQuestion)
