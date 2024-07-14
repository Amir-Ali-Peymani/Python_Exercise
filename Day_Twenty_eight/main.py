import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_lable.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    count_down(work_sec)
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_lable.config(text="Break", fg=RED)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        title_lable.config(text="Break", fg=PINK)
    else:
        count_down(5*60)
        title_lable.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec == f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=PINK)

title_lable = tkinter.Label(text="Timer", fg=GREEN,bg=PINK,  font=(FONT_NAME, 50))
title_lable.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="D:\Projects\Python\Python_Exercise\Day_Twenty_eight\\tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)


statr_button = tkinter.Button(text="Start", command=start_timer)
statr_button.grid(column=0, row=4)

reset_button = tkinter.Button(text="Reset")
reset_button.grid(column=2, row=4)

check_marks = tkinter.Label(fg=GREEN, bg=PINK, font=(100))
check_marks.grid(column=1, row=5)

window.mainloop()

