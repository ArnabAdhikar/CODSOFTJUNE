from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("iQuiz App")
        self.window.geometry("850x530")
        self.display_title()
        self.canvas = Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(400, 125,
                                                     text="Question here",
                                                     width=680,
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'Ariel', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()
        self.user_answer = StringVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.place(x=300, y=380)
        self.buttons()
        self.window.mainloop()
    def display_title(self):
        title = Label(self.window, text="iQuiz Application",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)
    def display_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
    def radio_buttons(self):
        choice_list = []
        y_pos = 220
        while len(choice_list) < 4:
            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer,
                                    value='', font=("ariel", 14))
            choice_list.append(radio_btn)
            radio_btn.place(x=200, y=y_pos)
            y_pos += 40
        return choice_list
    def display_options(self):
        val = 0
        self.user_answer.set(None)
        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1
    def next_btn(self):
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Correct answer! \U0001F44D'
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('\u274E Oops! \n'
                                     f'The right answer is: {self.quiz.current_question.correct_answer}')
        if self.quiz.has_more_questions():
            self.display_question()
            self.display_options()
        else:
            self.display_result()
            self.window.destroy()
    def buttons(self):
        next_button = Button(self.window, text="Next", command=self.next_btn,
                             width=10, bg="green", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=460)
        quit_button = Button(self.window, text="Quit", command=self.window.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))
        quit_button.place(x=700, y=50)
    def display_result(self):
        correct, wrong, score_percent = self.quiz.get_score()
        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"
        result = f"Score: {score_percent}%"
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")
