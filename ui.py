from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text=f"Score:", bg=THEME_COLOR, fg="white", font=("Arial", 20, "italic"))
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", width=300, height=250,highlightthickness=0)
        self.text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="31",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="true.png")
        self.right_button = Button(image=self.true_image, highlightthickness=0, command=self.is_true)
        self.right_button.grid(row=2, column=0)

        self.wrong_image = PhotoImage(file="false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, command=self.is_false)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=f"{q_text}")
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


