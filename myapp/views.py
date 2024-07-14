from django.shortcuts import render, redirect
from .models import Question, QuizResponse, QuizResult
from .forms import QuizForm

def quiz_view(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = 0
            for i, question in enumerate(questions):
                selected_option = form.cleaned_data[f'question_{i}']
                correct = selected_option == question.correct_option
                if correct:
                    score += 1
                QuizResponse.objects.create(
                    question=question,
                    selected_option=selected_option,
                    correct=correct
                )
            QuizResult.objects.create(score=score)
            return redirect('quiz_success', score=score)
    else:
        form = QuizForm(questions=questions)

    return render(request, 'quiz.html', {'form': form})

def quiz_success(request, score):
    return render(request, 'quiz_success.html', {'score': score})
