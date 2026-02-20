#interface.py

import tkinter as tk
from indice import colar_texto

def callback_button1():
    colar_texto('chave_1')

def criar_interface():
    janela = tk.Tk()
    janela.title("Repyta")
    janela.geometry("500x800")
    janela.resizable(False, False)

    frame_principal = tk.Frame(janela, padx=10, pady=10)
    frame_principal.pack(fill=tk.BOTH, expand=True)
    frame_principal.columnconfigure(1, weight=1)  
    frame_principal.rowconfigure(1, weight=1)     

    titulo = tk.Label(frame_principal, text="Botões de Atalho", font=("Arial", 14, "bold"))
    titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

    canvas = tk.Canvas(frame_principal, height=620)
    scrollbar = tk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    frame_botoes = tk.Frame(canvas)
    
    frame_botoes.columnconfigure(0, weight=1)  # Espaçador esquerdo
    frame_botoes.columnconfigure(1, weight=0)  # Coluna botões esquerda
    frame_botoes.columnconfigure(2, weight=0)  # Coluna botões direita
    frame_botoes.columnconfigure(3, weight=1)  # Espaçador direito

    canvas_window = canvas.create_window((0, 0), window=frame_botoes, anchor="nw")

    def _on_mousewheel(event):
        if event.num == 4 or event.delta > 0:
            canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            canvas.yview_scroll(1, "units")
        return "break"

    canvas.bind_all("<Button-4>", _on_mousewheel)
    canvas.bind_all("<Button-5>", _on_mousewheel)
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    frame_botoes.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.bind("<Configure>", lambda e: frame_botoes.configure(width=e.width))

    scrollbar.grid(row=1, column=0, sticky="ns") 
    canvas.grid(row=1, column=1, sticky="nsew")   

    botoes = [
        ("nome_do_botao_1", callback_button1),
    ]

    for i, (texto, comando) in enumerate(botoes):
        linha = (i // 2) + 1
        coluna = i % 2
        btn = tk.Button(
            frame_botoes,
            text=texto,
            command=comando,
            width=25,
            height=3,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 9),
            relief=tk.RAISED,
            cursor="hand2",
            wraplength = 180

        )
        btn.grid(row=linha, column=coluna, padx=5, pady=5, sticky="ew")

    btn_fechar = tk.Button(
        frame_principal,
        text="Fechar",
        command=janela.destroy,
        width=20,
        height=2,
        bg="#f44336",
        fg="white",
        font=("Arial", 10, "bold")
    )
    btn_fechar.grid(row=len(botoes) // 2 + 2, column=0, columnspan=2, pady=15)

    instrucao = tk.Label(
        frame_principal,
        text="Clique onde deseja colar o texto\nantes de usar os botões",
        font=("Arial", 8, "italic"),
        fg="#666"
    )
    instrucao.grid(row=len(botoes) // 2 + 3, column=0, columnspan=2, pady=(10, 0))

    janela.mainloop()


    #9
if __name__ == "__main__":
    criar_interface()
