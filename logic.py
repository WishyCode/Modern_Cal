import tkinter as tk
from PIL import ImageTk, Image

calcculation = "" 

def add_to_calculation(symbol):
    global calcculation
    calcculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0, calcculation)

def evaluate_calculation():
    global calcculation
    try:
        calcculation = str(eval(calcculation))   
        text_result.delete(1.0,"end")
        text_result.insert(1.0, calcculation)
    except:
        clear_fields()
        text_result.insert(1.0, "Error")

def clear_fields():
    global calcculation
    calcculation = ""
    text_result.delete(1.0,"end")

root = tk.Tk()
root.geometry("400x600+500+100")
root.resizable(False, False)
root.config(bg="#EAEAEA")
root.title("Calculator")

my_image=ImageTk.PhotoImage(file="E:/GITRepo/20250719_python_cal/Calculator_bg.jpg")
lbl_image=tk.Label(root, image=my_image,bg="#EAEAEA").place(x=0, y=0) 

text_result = tk.Text(root, height=2, font=("times", 32,'bold'), bg="#E8E8E8", bd=0, fg="#525252")
text_result.place(x=25, y=58, width=350, height=45)

btn_1 = tk.Button(root, text="1", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("1"))
btn_1.place(x=41, y=133, width=42, height=42)
btn_2 = tk.Button(root, text="2", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("2"))
btn_2.place(x=134, y=133, width=42, height=42)
btn_3 = tk.Button(root, text="3", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("3"))
btn_3.place(x=227, y=133, width=42, height=42)
btn_plus = tk.Button(root, text="+", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("+"))
btn_plus.place(x=320, y=133, width=42, height=42)
btn_4 = tk.Button(root, text="4", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("4"))
btn_4.place(x=41, y=227, width=42, height=42)
btn_5 = tk.Button(root, text="5", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("5"))
btn_5.place(x=134, y=227, width=42, height=42)
btn_6 = tk.Button(root, text="6", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("6"))
btn_6.place(x=227, y=227, width=42, height=42)
btn_minus = tk.Button(root, text="-", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("-"))
btn_minus.place(x=320, y=224, width=42, height=42)
btn_7 = tk.Button(root, text="7", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("7"))
btn_7.place(x=41, y=321, width=42, height=42)
btn_8 = tk.Button(root, text="8", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("8"))
btn_8.place(x=134, y=321, width=42, height=42)
btn_9 = tk.Button(root, text="9", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("9"))
btn_9.place(x=227, y=321, width=42, height=42)
btn_div = tk.Button(root, text="/", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("/"))
btn_div.place(x=320, y=321, width=42, height=42)
btn_open = tk.Button(root, text="(", font=("times", 28, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("("))
btn_open.place(x=40, y=413, width=42, height=42)
btn_0 = tk.Button(root, text="0", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("0"))
btn_0.place(x=134, y=415, width=42, height=42)
btn_close = tk.Button(root, text=")", font=("times", 28, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation(")"))
btn_close.place(x=229, y=413, width=42, height=42)
btn_multi = tk.Button(root, text="x", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command=lambda: add_to_calculation("*"))
btn_multi.place(x=320, y=410, width=42, height=42)

btn_clean = tk.Button(root, text="Clean", font=("times", 24, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command= clear_fields)
btn_clean.place(x=65, y=515, width=100, height=28)
btn_equal = tk.Button(root, text="=", font=("times", 36, 'bold'), bg="#E8E8E8", fg="#525252", bd=0, activebackground="#E8E8E8", command= evaluate_calculation)
btn_equal.place(x=281, y=507, width=42, height=42)

root.mainloop()