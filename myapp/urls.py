from django.urls import path
from .views import quiz_view, quiz_success

urlpatterns = [
    path('quiz/', quiz_view, name='quiz'),
    path('quiz_success/<int:score>/', quiz_success, name='quiz_success'),
]
