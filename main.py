from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random

question_bank = []

for question in question_data:
    question_bank.append(Question(question=question["question"], answer=question["correct_answer"]))

random.shuffle(question_bank)

quiz = QuizBrain(question_bank)

while True:

    quiz.next_question()

    if not quiz.check_answer():
        quiz.wrong()
    else:
        quiz.correct()

    print("\n")

    if not quiz.still_has_questions():
        print(f"You have completed the quiz!")
        print(f"Your final score is: {quiz.score}/{quiz.question_number+1}")
        break

    quiz.question_number += 1

