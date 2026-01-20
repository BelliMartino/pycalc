import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            # eval() valuta la stringa come un'espressione matematica
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Errore", "Input non valido")
            entry.delete(0, tk.END)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Configurazione finestra principale
root = tk.Tk()
root.title("Calcolatrice")

# Campo di testo per visualizzare i numeri
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=5, relief="flat", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definizione dei bottoni
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Creazione e posizionamento bottoni
row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: on_click(x)
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 14),
              command=action).grid(row=row_val, column=col_val, padx=2, pady=2)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()