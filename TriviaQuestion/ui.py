from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Trivia Question")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", background=THEME_COLOR)
        self.score_label.grid(row=0, column=5)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Word",
            font=("Arial", 20, "italic"),
            fill="black",
            width=200
        )
        self.canvas.grid(row=4, column=0, columnspan=6, pady=50)

        false_image = PhotoImage(file="images/false.png")
        true_image = PhotoImage(file="images/true.png")

        self.true_button = Button(image=true_image, command=self.true_pressed, highlightthickness=0)
        self.true_button.grid(row=6, column=4, columnspan=3)

        self.false_button = Button(image=false_image, command=self.false_pressed, highlightthickness=0)
        self.false_button.grid(row=6, column=0, columnspan=3)

        self.get_next_question()

        self.window.mainloop()

    def false_pressed(self):
        self.check_answer("False")

    def true_pressed(self):
        self.check_answer("True")

    def check_answer(self, answer):
        self.update_score(self.quiz.check_answer(answer))

    def get_next_question(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.end_quiz()

    def update_score(self, is_right):
        if is_right:
            self.canvas.configure(bg='green')
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.configure(bg='red')

        self.window.after(1000, self.get_next_question)

    def end_quiz(self):
        q_text = f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}"
        self.canvas.itemconfig(self.question_text, text=q_text, font=("Arial", 30, "italic"))
        self.true_button.config(state="disable")
        self.false_button.config(state="disable")

        self.window.after(5000, self.window.quit)
