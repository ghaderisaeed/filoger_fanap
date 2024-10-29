import tkinter as tk
import random
from tkinter import messagebox

# Generate a random number between 1 and 100
LOWER = 1
UPPER = 100
computer_guess = random.randint(LOWER, UPPER)

window = tk.Tk()
window.geometry('600x500')
window.title('بازی حدس اعداد')
window.resizable(width=False,height=False)
window.config(bg='#BFCFE7')



def attempts_check():
     global attempts
     attempts = scale_attempts.get()
     attempts_btn.config(state=tk.DISABLED)
     guess_btn.config(state=tk.NORMAL)
     
     
def showexit():
    result = messagebox.askquestion('خروج', 'آیا میخواهید از برنامه خارج شوید؟')
    if result == "yes":
    	window.destroy()


def restart():
    global computer_guess
    global attempts
    
    computer_guess = random.randint(LOWER, UPPER)
    guess_btn.config(state=tk.DISABLED)
    attempts_btn.config(state=tk.NORMAL)
    win_lose_label.set("")
    user_guess_label.set("")
    # print(computer_guess)


def guessnumber():
    global user
    global attempts
    attempts -=1

    try:
        user_guess = int(user.get())
        if user_guess > 100 or user_guess < 1:
            messagebox.showwarning('اخطار', 'لطفا یک عدد بین 1 تا 100 وارد کنید')
            attempts +=1
        elif user_guess == computer_guess:
            win_lose_label.set("آفرین! شما برنده شدید")
            user_guess_label.set('')
            label_win_lose_.config(fg='green', font=('Times New Roman', 17,'bold'))
            label_win_lose_.place(x=200, y=250)
            guess_btn.config(state=tk.DISABLED)

        elif attempts==0:
            win_lose_label.set(f"!شما باختید. عدد درست {computer_guess} بود ")
            user_guess_label.set('')
            label_win_lose_.config(fg='red', font=('Times New Roman', 17,'bold'))
            label_win_lose_.place(x=175, y=250)
            guess_btn.config(state=tk.DISABLED)

        elif user_guess < computer_guess:
            user_guess_label.set(f'عدد شما کوچکتر است \n\n شما {attempts} فرصت دارید')
        else:
            user_guess_label.set(f'عدد شما بزرگتر است\n\n شما {attempts} فرصت دارید')

    except:
        messagebox.showwarning('اخطار', 'لطفا یک عدد بین 1 تا 100 وارد کنید')
        attempts +=1

    return


label = tk.Label(window, text=":لطفا یک عدد بین ۱ تا ۱۰۰ حدس بزنید", font=('Times New Roman', 13, 'bold'), anchor="center", bg='#BFCFE7')
label.place(x=300, y=50)

user_variable = tk.StringVar()
user = tk.Entry(window, textvariable=user_variable, font=('Times New Roman', 14), borderwidth=5)
user.place(x=325, y=100)

user_guess_label = tk.StringVar()
label_user_guess = tk.Label(window, textvariable=user_guess_label, font=('Times New Roman', 17), bg='#BFCFE7',)
label_user_guess.place(x=220, y=225)

win_lose_label = tk.StringVar()
label_win_lose_ = tk.Label(window, textvariable=win_lose_label, font=('Times New Roman', 14), bg='#BFCFE7')

guess_btn = tk.Button(window, text="حدس بزن", font=('Times New Roman', 14), command=guessnumber, bg='#BFCFE7', borderwidth=5)
guess_btn.place(x=300, y=350)
guess_btn.config(state=tk.DISABLED)

restart_btn = tk.Button(window, text="شروع مجدد", font=('Times New Roman', 14), command=restart, bg='#BFCFE7', borderwidth=5)
restart_btn.place(x=200, y=350)


exit_btn = tk.Button(window, text="خروج", font=('Times New Roman', 14), command=showexit, bg='#BFCFE7', borderwidth=5)
exit_btn.place(x=260, y=425)

scale_attempts = tk.Scale(window, from_=5, to=10, orient=tk.HORIZONTAL, bg='#BFCFE7', borderwidth=5)
scale_attempts.place(x=70, y=80)

label_attempts = tk.Label(window, text=":لطفا تعداد فرصت‌های خود را انتخاب کنید", font=('Times New Roman', 11, 'bold'), bg='#BFCFE7')
label_attempts.place(x=25, y=50)

attempts_btn = tk.Button(window, text='انتخاب', font=('Times New Roman', 12, 'bold'), command=attempts_check, bg='#BFCFE7', borderwidth=5)
attempts_btn.place(x=100, y=150)


window.mainloop()