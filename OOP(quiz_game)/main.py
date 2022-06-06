from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q_a in question_data:
    question_text = q_a["text"]
    question_answer = q_a["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your score is {quiz.score}/{quiz.question_number}")
