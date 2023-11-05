import tkinter as tk


def calcular():
    try:
        resultado = eval(entry.get())
        resultado_label.config(text="Resultado: " + str(resultado))
    except Exception as e:
        resultado_label.config(text="Erro: " + str(e))


# Configuração da janela
janela = tk.Tk()
janela.title("Calculadora")

# Entrada de texto
entry = tk.Entry(janela)
entry.pack()

# Botões
botoes = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', 'C', '=', '/'
]

frame = tk.Frame(janela)
frame.pack()

row, col = 0, 0

for botao in botoes:
    tk.Button(frame, text=botao, width=5, height=2,
              command=lambda b=botao: entry.insert('end', b) if b != 'C' else entry.delete(0, 'end')).grid(row=row,
                                                                                                           column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Botão de cálculo
calcular_botao = tk.Button(janela, text="Calcular", command=calcular)
calcular_botao.pack()

# Resultado
resultado_label = tk.Label(janela, text="Resultado: ")
resultado_label.pack()

janela.mainloop()
