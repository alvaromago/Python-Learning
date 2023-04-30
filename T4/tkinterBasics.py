import tkinter

ventana = tkinter.Tk()  # Definición de una ventana
ventana.geometry("500x400")  # Tamaño

## Label ##
lbl1 = tkinter.Label(ventana, text="Hola Mundo")
lbl1.pack()  # Poner 'etiqueta' en la pantalla
lbl2 = tkinter.Label(ventana, text="Texto inferior", bg="grey")
lbl2.pack(side=tkinter.BOTTOM)


def saludo():
    print("Hola")


## Button ##
# La llamada a la función debe ir sin paréntesis
btn1 = tkinter.Button(ventana, text="Pulsa", command=saludo)
btn1.pack()

## TextField ##

ventana.mainloop()
