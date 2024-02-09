from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"
class QuizeInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.screen = Tk()
        self.quiz = quiz_brain
        self.screen.title("Quizzer")
        self.screen.config(bg='black', padx=100, pady=40)
        self.label_score = Label(text="Score: 0", bg='black', highlightthickness=0, fg='white',
                                 font=("Arial", 20, 'bold'))
        self.label_score.grid(row=0, column=2)

        self.canvas = Canvas(width=450, height=400, bg='white')
        self.question = self.canvas.create_text(200, 170,
                                                width=400,
                                                text="questions here!",
                                                font=("Arial", 15, 'italic'), fill='black')
        self.canvas.grid(column=1, row=2, columnspan=2)
        img_right = PhotoImage(file="images/true.png")
        self.button_right = Button(text="right", image=img_right, highlightthickness=0, bg='black', command=self.true_pressed)
        self.button_right.grid(row=3, column=1)

        img_wrong = PhotoImage(file="images/false.png")

        self.button_wrong = Button(text="wrong", image=img_wrong, bg='black', highlightthickness=0, command= self.false_pressed)

        self.button_wrong.grid(row=3, column=2)
        self.get_next_question()
        self.screen.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label_score.config(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
            self.canvas.itemconfig(self.question, text=q_text)
            self.canvas.config(bg='white')
        else:
            self.canvas.itemconfig(self.question, text=f"You've reached the end of the question.")
            self.button_right.config(state=DISABLED)
            self.button_wrong.config(state=DISABLED)
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.screen.after(1000, self.get_next_question)