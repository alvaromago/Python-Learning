import tkinter

v = tkinter.Tk()
v.geometry("400x300")

btn1 = tkinter.Button(v, text="Boton1", width=7, height=2)
btn2 = tkinter.Button(v, text="Boton2", width=7, height=2)
btn3 = tkinter.Button(v, text="Boton3", width=7, height=2)

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)

v.mainloop()
