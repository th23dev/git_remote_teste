import tkinter as tk
from tkinter import messagebox

def calcular():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    opcao = int(var_opcao.get())

    if opcao == 1:
        resultado = num1 + num2
        messagebox.showinfo("Resultado", f"O resultado da adição é: {resultado}")
    elif opcao == 2:
        resultado = num1 - num2
        messagebox.showinfo("Resultado", f"O resultado da subtração é: {resultado}")
    elif opcao == 3:
        resultado = num1 * num2
        messagebox.showinfo("Resultado", f"O resultado da multiplicação é: {resultado}")
    elif opcao == 4:
        resultado = num1 / num2
        messagebox.showinfo("Resultado", f"O resultado da divisão é: {resultado}")

root = tk.Tk()
root.title("Calculadora")

label_num1 = tk.Label(root, text="Digite o primeiro número:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Digite o segundo número:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

label_opcao = tk.Label(root, text="Escolha a operação:")
label_opcao.pack()
var_opcao = tk.StringVar()
radio_adicao = tk.Radiobutton(root, text="Adição", variable=var_opcao, value=1)
radio_adicao.pack()
radio_subtracao = tk.Radiobutton(root, text="Subtração", variable=var_opcao, value=2)
radio_subtracao.pack()
radio_multiplicacao = tk.Radiobutton(root, text="Multiplicação", variable=var_opcao, value=3)
radio_multiplicacao.pack()
radio_divisao = tk.Radiobutton(root, text="Divisão", variable=var_opcao, value=4)
radio_divisao.pack()

button_calcular = tk.Button(root, text="Calcular", command=calcular)
button_calcular.pack()

root.mainloop()