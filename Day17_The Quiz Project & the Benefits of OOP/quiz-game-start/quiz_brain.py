#TODO: asking the questions
#TODO: checking if the answer was correct
#TODO: checking if we're at the end of the quiz.

class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        print("reach inside quiz_brain")
    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer.upper()
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question} ").upper()
        return self.check_answer(user_answer,current_answer)
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
            
    def check_answer(self,user_answer,current_answer):
        if user_answer == current_answer:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {current_answer}.")
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
            return True
        else:
            print("You got it wrong!")
            return False




# while self.next_question(i,question_list):

#             print("Balle Balle!")
#         else:
#             print("Thalle Thalle")
#             break
    
    