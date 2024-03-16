import tkinter as tk

control = 0
control2 = 0

def on():
    global control, control2
    control += 1
    control2 += 1
    print(control, control2)
    
    cont1.config(text="Включено")
    
    if control2 == 1 or control == 1:
        cont.config(text=" ")
    
    if control == 20:
        cont.config(text="Проверьте контакты")
        control = 0
    
    if control2 == 100:
        cont.config(text="Проверьте контакты, слишком большое количетво использования станка")
        control2 = 0

    
def off():
    cont1.config(text="Выключенно")


root = tk.Tk()

cont1 = tk.Label(root, text=" ")
cont1.pack()


cont = tk.Label(root, text="")
cont.pack()

buttonOn = tk.Button(root, text="On", command=(lambda: on()))
buttonOn.pack()

buttonOff = tk.Button(root, text="Off", command=off)
buttonOff.pack()


root.mainloop()