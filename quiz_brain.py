class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.answer = ""
        self.score = 0

    def next_question(self):
        while True:
            self.answer = input(
                f'Q.{self.question_number + 1}: {self.question_list[self.question_number].question} (True'
                f'/False): ').capitalize()
            if self.answer == "True" or self.answer == "False":
                break

    def check_answer(self):
        return self.answer == self.question_list[self.question_number].answer

    def correct(self):
        self.score += 1
        print("That if correct.")
        print(f"The correct answer is {self.question_list[self.question_number].answer}.")
        print(f"Your current score is {self.score}/{self.question_number + 1}")

    def wrong(self):
        self.score += 0
        print("That is wrong.")
        print(f"The correct answer is {self.question_list[self.question_number].answer}.")
        print(f"Your current score is {self.score}/{self.question_number + 1}")

    def still_has_questions(self):
        return self.question_number < (len(self.question_list) - 1)



