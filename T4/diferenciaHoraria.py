import tkinter

v = tkinter.Tk()
v.geometry("310x70")

lblHH1 = tkinter.Label(v, text="HH")
lblHH2 = tkinter.Label(v, text="HH")
lblMM1 = tkinter.Label(v, text="MM")
lblMM2 = tkinter.Label(v, text="MM")
txtHH1 = tkinter.Entry(v)
txtHH2 = tkinter.Entry(v)
txtMM1 = tkinter.Entry(v)
txtMM2 = tkinter.Entry(v)
btnCalcular = tkinter.Button(v, text="Calcular")
txtResultado = tkinter.Entry(v)

lblHH1.grid(row=0, column=0)
txtHH1.grid(row=0, column=1)
lblMM1.grid(row=0, column=2)
txtMM1.grid(row=0, column=3)
lblHH2.grid(row=1, column=0)
txtHH2.grid(row=1, column=1)
lblMM2.grid(row=1, column=2)
txtMM2.grid(row=1, column=3)
btnCalcular.grid(row=2, column=0)
txtResultado.grid(row=2, column=1)

v.mainloop()
