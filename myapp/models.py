from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1, choices=[
        ('a', 'Option A'),
        ('b', 'Option B'),
        ('c', 'Option C'),
        ('d', 'Option D'),
    ])

    def __str__(self):
        return self.text

class QuizResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1, choices=[
        ('a', 'Option A'),
        ('b', 'Option B'),
        ('c', 'Option C'),
        ('d', 'Option D'),
    ])
    correct = models.BooleanField()

    def __str__(self):
        return f"Response to: {self.question.text}"

class QuizResult(models.Model):
    score = models.IntegerField()

    def __str__(self):
        return f"Score: {self.score}"
