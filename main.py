import json
from tkinter import *
from tkinter import Radiobutton
from tkinter import messagebox as mb

root = Tk()

root.state('zoomed')
root.title('Quizz')
root.config(bg='#fff')
root.iconbitmap("./img/logo.ico")

font = ('san-serif', 16, 'bold')

with open('data.json') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])

que_no = 0
opt_selected = IntVar()
correct = 0
data_size = len(question)


def display_question():
    q_no = Label(root, text=question[que_no], width=60,
                 font=(font, 16), anchor='w', bg='white')
    q_no.place(x=300, y=150)


def display_options():
    opts = radio_buttons()
    val = 0
    opt_selected.set(0)
    for option in options[que_no]:
        opts[val]['text'] = option
        val += 1


def radio_buttons():
    q_list = []
    y_pos = 250
    while len(q_list) < 4:
        radio_btn = Radiobutton(root, variable=opt_selected, value=len(
            q_list) + 1, font=(font, 16), bg='white')
        q_list.append(radio_btn)
        radio_btn.place(x=300, y=y_pos)
        y_pos += 40
    return q_list


def next_btn():
    global correct
    global que_no
    if check_ans(que_no):
        correct += 1
    que_no += 1
    if que_no == data_size:
        btn_Next.destroy()
        mb.showwarning("Warning", "All Question are completed")
        btn_Result = Button(image=btnResult, border=0,
                            bg='white', borderwidth=0, command=display_result)
        btn_Result.pack(side=BOTTOM, pady=90)

    else:
        display_question()
        display_options()


def start_btn():
    label1.destroy()
    title.destroy()
    btn_Start.destroy()
    display_question()
    display_options()


def check_ans(q_no):
    global correct
    global que_no
    if opt_selected.get() == answer[q_no]:
        return True
    if not opt_selected.get():
        mb.showwarning("Warning", "Please select a option")
        que_no -= 1


def display_result():
    wrong_count = data_size - correct
    correct_count = int(correct)
    score = int(correct_count / data_size * 100)
    label2 = Label(image=thanks, border=0)
    label2.place(x=0, y=0)
    correct_label = Label(text='Your Score', font=(font, 30), bg="#FDBC00")
    correct_label.place(x=1000, y=200)
    correct_label = Label(
        text=f'Correct: {correct}', font=(font, 30), bg="#FDBC00")
    correct_label.place(x=1000, y=300)
    wrong_label = Label(
        text=f'Wrong: {wrong_count}', font=(font, 30), bg="#FDBC00")
    wrong_label.place(x=1000, y=400)
    result_label = Label(
        text=f'Score: {score}%', font=(font, 30), bg="#FDBC00")
    result_label.place(x=1000, y=500)


btnResult = PhotoImage(file="img/Result.png")
thanks = PhotoImage(file="./img/image 2.png")
bg = PhotoImage(file="./img/MacBook Air - 4.png")
label1 = Label(image=bg, bg='white', border=0)
label1.place(x=0, y=0)

title_img = PhotoImage(file="./img/Group 6.png")
title = Label(image=title_img, bg='white', border=0)
title.pack(pady=50)

quizz_img = PhotoImage(file="img/image 1.png")
label1 = Label(image=quizz_img, border=0, bg='white')
label1.pack()

btnStart = PhotoImage(file="img/Start.png")
btn_Start = Button(image=btnStart, border=0, bg='white',
                   borderwidth=0, command=start_btn)
btn_Start.pack(pady=80)

btnNext = PhotoImage(file="img/Next.png")
btn_Next = Button(image=btnNext, border=0, bg='white',
                  borderwidth=0, command=next_btn)
btn_Next.pack(side=BOTTOM, pady=90)


root.mainloop()
