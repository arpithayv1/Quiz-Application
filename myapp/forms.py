from django import forms
from .models import Question

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)
        for i, question in enumerate(questions):
            self.fields[f'question_{i}'] = forms.ChoiceField(
                choices=[
                    ('a', question.option_a),
                    ('b', question.option_b),
                    ('c', question.option_c),
                    ('d', question.option_d)
                ],
                label=question.text,
                widget=forms.RadioSelect
            )
