from django.contrib import admin
from .models import Question, QuizResponse, QuizResult

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'correct_option')

@admin.register(QuizResponse)
class QuizResponseAdmin(admin.ModelAdmin):
    list_display = ('question', 'selected_option', 'correct')

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('score',)
