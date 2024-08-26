# Django Simple Quiz Application

## Overview
This is a Django-based quiz application where users can answer multiple-choice questions. The application tracks the user's responses and calculates their score. The quiz questions, options, and correct answers are managed through Django's admin interface.

## Objectives
- **Create and Manage Questions:** Provide an interface for creating and managing multiple-choice questions, including specifying the correct option.
- **Collect Quiz Responses:** Enable users to select answers for each question and record their responses.
- **Calculate Quiz Results:** Automatically calculate the user's score based on the correctness of their responses.

## Technologies Used
- **Django:** The web framework used for the backend, including models, views, and forms.
- **HTML/CSS:** For rendering and styling the quiz interface.
- **JavaScript:** Adds interactivity to the quiz experience.
- **SQLite:** Default database for storing questions, responses, and scores.

## Models
- **Question:**
  - Stores the text of the question and the four possible answer options (A, B, C, D).
  - Tracks which of the options is the correct answer.
  
- **QuizResponse:**
  - Records the user's selected option for each question.
  - Tracks whether the selected option is correct.

- **QuizResult:**
  - Stores the user's total score after completing the quiz.

## Forms
- **QuizForm:**
  - Dynamically generates a form with multiple-choice fields based on the questions in the quiz.
  - Uses radio buttons to allow users to select one answer per question.

## Admin Interface
- The Django admin interface is used to add, edit, and delete questions and their answer options. Admins can also review user responses and scores.

## Usage
- **Admin:** Use the Django admin interface to create questions, set correct answers, and manage the quiz content.
- **User:** Access the quiz, answer the questions, and submit responses to see the score.
