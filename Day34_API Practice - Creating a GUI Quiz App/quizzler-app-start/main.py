from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html
from ui import QuizInterface
question_bank = []

WHITE = "#ffffff"
BLACK = "#000000"

# print(question_data)
for question in question_data:
    print("tiki tiki pheki pheki")
    question_text = question["question"]
    # question_text = html.unescape(question_text)
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    # quiz_ui.canvas.itemconfig(question_text,text=question_text,fill=BLACK)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

