from textblob import TextBlob
from tkinter import *

def correct_spelling():
    try:
        get_data = entry1.get()
        corr = TextBlob(get_data)
        data = corr.correct()
        entry2.config(state="normal")
        entry2.delete(0, END)
        entry2.insert(0, data)
        entry2.config(state="readonly")
    except Exception as e:
        print(f"Error: {e}")

def main_window():
    global entry1, entry2
    
    win = Tk()
    win.geometry("500x400")
    win.resizable(False, False)
    win.config(bg="Blue")
    win.title("Spell Checker")
    
    title_label = Label(win, text="Spell Checker", font=("Arial", 30, "bold"), bg="#2980b9", fg="white")
    title_label.place(x=50, y=10, width=400, height=50)
    
    label1 = Label(win, text="Incorrect Spelling:", font=("Arial", 18, "bold"), bg="#3498db", fg="white")
    label1.place(x=50, y=80)
    
    entry1 = Entry(win, font=("Arial", 15), borderwidth=2, relief="groove")
    entry1.place(x=50, y=120, width=400, height=35)
    
    label2 = Label(win, text="Corrected Spelling:", font=("Arial", 18, "bold"), bg="#3498db", fg="white")
    label2.place(x=50, y=170)
    
    entry2 = Entry(win, font=("Arial", 15), borderwidth=2, relief="groove")
    entry2.place(x=50, y=210, width=400, height=35)
    entry2.config(state="readonly")
    
    button = Button(win, text="Correct", font=("Arial", 15, "bold"), bg="#2ecc71", fg="white", activebackground="#27ae60", command=correct_spelling)
    button.place(x=200, y=270, width=100, height=40)
    
    win.mainloop()

main_window()
