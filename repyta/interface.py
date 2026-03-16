# interface.py
# =====================================================#
## Interface com botões para substituir atalhos de teclado ##
# =====================================================#

import indice
import tkinter as tk
from tkinter import messagebox, filedialog
import json
from indice import proxima_chave, criar_callback_com_chave, set_estado_automacoes

# ✅ Variáveis para sistema de rótulos
rotulo_filtro_atual = None  # None = mostra todos
combobox_rotulos_ref = None  # Referência ao combobox de rótulos
lista_rotulos_criados = []   # Lista de rótulos já utilizados

# Variável global para controle de navegação
tela_atual = None

# ✅ Variáveis para controle de modo de edição
edit_mode = False
chave_edicao_atual = None
btn_salvar_ref = None  # Referência ao botão de salvar para modificar seu comportamento


# =====================================================#
## 2 Funções de callback para os botões ##
# =====================================================#

def voltar_para_painel_de_botoes():
    """Volta para o painel principal de botões"""
    mostrar_tela("painel_botoes")


def abrir_painel_adicao_automacao():
    """Abre o painel de adição de automação"""
    mostrar_tela("painel_adicao_automacao")


def abrir_painel_texto_area_transferencia():
    """Abre o painel de adição de texto para área de transferência"""
    mostrar_tela("painel_texto_area_transferencia")


def salvar_texto_para_area_de_transferencia():
    """Salva o novo botão de texto para área de transferência"""
    global botoes, TEXTOS_PARA_COLAR, ROTULOS_POR_BOTAO, lista_rotulos_criados

    nome_botao = entry_nome_botao.get().strip()
    texto_conteudo = entry_texto_conteudo.get("1.0", tk.END).strip()
    rotulos_input = combobox_rotulos_ref.get().strip() if combobox_rotulos_ref else ""

    if not nome_botao:
        messagebox.showerror("Erro", "Por favor, digite um nome para o botão.")
        return

    if not texto_conteudo:
        messagebox.showerror("Erro", "Por favor, digite o texto que será copiado.")
        return

    chave = proxima_chave()
    TEXTOS_PARA_COLAR[chave] = texto_conteudo

    # ✅ Processa e salva rótulos
    if rotulos_input:
        rotulos_lista = [r.strip() for r in rotulos_input.split(',') if r.strip()]
        ROTULOS_POR_BOTAO[chave] = rotulos_lista
        # Atualiza lista global de rótulos únicos
        for r in rotulos_lista:
            if r not in lista_rotulos_criados:
                lista_rotulos_criados.append(r)

    callback = criar_callback_com_chave(chave)
    botoes.append((nome_botao, callback))

    # Limpa os campos
    entry_nome_botao.delete(0, tk.END)
    entry_texto_conteudo.delete("1.0", tk.END)
    if combobox_rotulos_ref:
        combobox_rotulos_ref.delete(0, tk.END)

    messagebox.showinfo("Sucesso", f"Botão '{nome_botao}' adicionado com sucesso!")
    atualizar_painel_botoes()
    voltar_para_painel_de_botoes()


# =====================================================#
## Funções para menu contextual (Editar/Apagar) ##
# =====================================================#

def mostrar_menu_contextual(event, chave, nome_botao):
    """Exibe menu contextual com opções Editar e Apagar ao clicar com botão direito"""
    menu = tk.Menu(janela, tearoff=0, font=("Arial", 9))
    menu.add_command(label="✏️ Editar", command=lambda: editar_botao_texto(chave, nome_botao))
    menu.add_command(label="🗑️ Apagar", command=lambda: apagar_botao_texto(chave))
    menu.tk_popup(event.x_root, event.y_root)
    menu.bind("<FocusOut>", lambda e: menu.destroy())  # Fecha menu ao perder foco


def editar_botao_texto(chave, nome_botao):
    """Prepara o painel para edição de um botão existente"""
    global edit_mode, chave_edicao_atual, btn_salvar_ref

    edit_mode = True
    chave_edicao_atual = chave

    mostrar_tela("painel_texto_area_transferencia")

    entry_nome_botao.delete(0, tk.END)
    entry_nome_botao.insert(0, nome_botao)

    entry_texto_conteudo.delete("1.0", tk.END)
    entry_texto_conteudo.insert("1.0", TEXTOS_PARA_COLAR.get(chave, ""))

    # ✅ Pré-preenche rótulos se existirem
    if combobox_rotulos_ref:
        combobox_rotulos_ref.delete(0, tk.END)
        rotulos_existentes = ROTULOS_POR_BOTAO.get(chave, [])
        if rotulos_existentes:
            combobox_rotulos_ref.insert(0, ", ".join(rotulos_existentes))

    if btn_salvar_ref:
        btn_salvar_ref.config(
            command=salvar_edicao_texto,
            text="💾 Atualizar",
            bg="#FF9800"
        )


def salvar_edicao_texto():
    """Salva as edições de um botão existente (mantendo a mesma chave)"""
    global edit_mode, chave_edicao_atual, btn_salvar_ref, ROTULOS_POR_BOTAO, lista_rotulos_criados

    nome_botao = entry_nome_botao.get().strip()
    texto_conteudo = entry_texto_conteudo.get("1.0", tk.END).strip()
    rotulos_input = combobox_rotulos_ref.get().strip() if combobox_rotulos_ref else ""

    if not nome_botao:
        messagebox.showerror("Erro", "Por favor, digite um nome para o botão.")
        return

    if not texto_conteudo:
        messagebox.showerror("Erro", "Por favor, digite o texto que será copiado.")
        return

    TEXTOS_PARA_COLAR[chave_edicao_atual] = texto_conteudo

    # ✅ Atualiza rótulos
    if rotulos_input:
        rotulos_lista = [r.strip() for r in rotulos_input.split(',') if r.strip()]
        ROTULOS_POR_BOTAO[chave_edicao_atual] = rotulos_lista
        for r in rotulos_lista:
            if r not in lista_rotulos_criados:
                lista_rotulos_criados.append(r)
    else:
        # Remove rótulos se campo estiver vazio
        ROTULOS_POR_BOTAO.pop(chave_edicao_atual, None)

    for i, (nome, callback) in enumerate(botoes):
        if hasattr(callback, 'chave') and callback.chave == chave_edicao_atual:
            botoes[i] = (nome_botao, callback)
            break

    edit_mode = False
    chave_edicao_atual = None
    if btn_salvar_ref:
        btn_salvar_ref.config(
            command=salvar_texto_para_area_de_transferencia,
            text="Salvar",
            bg="#4CAF50"
        )

    messagebox.showinfo("✅ Sucesso", f"Botão '{nome_botao}' atualizado com sucesso!")
    entry_nome_botao.delete(0, tk.END)
    entry_texto_conteudo.delete("1.0", tk.END)
    if combobox_rotulos_ref:
        combobox_rotulos_ref.delete(0, tk.END)
    atualizar_painel_botoes()
    voltar_para_painel_de_botoes()


def apagar_botao_texto(chave):
    """Apaga um botão e todos os seus dados associados"""
    confirmacao = messagebox.askyesno(
        "⚠️ Confirmar exclusão",
        "Tem certeza que deseja apagar este botão?\n\nEsta ação não pode ser desfeita."
    )
    if not confirmacao:
        return

    # Remove do dicionário de textos
    if chave in TEXTOS_PARA_COLAR:
        del TEXTOS_PARA_COLAR[chave]

    # ✅ Remove rótulos associados a este botão
    if chave in ROTULOS_POR_BOTAO:
        del ROTULOS_POR_BOTAO[chave]

    # Remove da lista de botões
    botoes[:] = [
        (nome, callback) for nome, callback in botoes
        if not (hasattr(callback, 'chave') and callback.chave == chave)
    ]

    # ✅ Opcional: Reorganizar lista_rotulos_criados (remove rótulos órfãos)
    # Isso mantém a lista de sugestões limpa
    from indice import ROTULOS_POR_BOTAO as rotulos_ativos
    rotulos_em_uso = set()
    for ch in rotulos_ativos.values():
        rotulos_em_uso.update(ch)
    global lista_rotulos_criados
    lista_rotulos_criados = [r for r in lista_rotulos_criados if r in rotulos_em_uso]

    messagebox.showinfo("✅ Sucesso", "Botão apagado com sucesso!")

    # Se estiver em modo de edição, cancelar a edição
    global edit_mode, chave_edicao_atual, btn_salvar_ref
    if edit_mode and chave_edicao_atual == chave:
        edit_mode = False
        chave_edicao_atual = None
        if btn_salvar_ref:
            btn_salvar_ref.config(
                command=salvar_texto_para_area_de_transferencia,
                text="Salvar",
                bg="#4CAF50"
            )
        entry_nome_botao.delete(0, tk.END)
        entry_texto_conteudo.delete("1.0", tk.END)

    atualizar_painel_botoes()


def resetar_edicao_se_necessario():
    """Reseta o modo de edição ao voltar do painel de texto"""
    global edit_mode, chave_edicao_atual, btn_salvar_ref

    if edit_mode:
        edit_mode = False
        chave_edicao_atual = None
        if btn_salvar_ref:
            btn_salvar_ref.config(
                command=salvar_texto_para_area_de_transferencia,
                text="Salvar",
                bg="#4CAF50"
            )
        entry_nome_botao.delete(0, tk.END)
        entry_texto_conteudo.delete("1.0", tk.END)


# =====================================================#
## Criação da interface gráfica ##
# =====================================================#

def criar_interface():
    global janela, frame_principal, canvas, frame_botoes
    global entry_nome_botao, entry_texto_conteudo

    janela = tk.Tk()
    janela.title("Repyta")

    # Obter dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Definir dimensões da janela (90% da tela com limites máximos)
    largura_janela = min(int(largura_tela * 0.70), 500)  # Máximo 600px de largura
    altura_janela = min(int(altura_tela * 0.85), 700)  # Máximo 700px de altura

    # Calcular posição para centralizar a janela
    pos_x = int((largura_tela - largura_janela) / 2)
    pos_y = int((altura_tela - altura_janela) / 2)

    # Aplicar geometria dinâmica e centralizada
    janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    # Permitir redimensionamento (opcional - o usuário pode ajustar se precisar)
    janela.resizable(True, True)

    # Definir tamanho mínimo para não ficar muito pequena
    janela.minsize(400, 600)

    # Frame principal com padding
    frame_principal = tk.Frame(janela, padx=30, pady=30)
    frame_principal.pack(fill=tk.BOTH, expand=True)

    # Configurar pesos do grid do frame_principal
    frame_principal.columnconfigure(0, weight=1)
    frame_principal.rowconfigure(1, weight=1)

    # Título
    global titulo_principal  # ✅ Adicionar esta linha
    titulo_principal = tk.Label(frame_principal, text="Painel de botões", font=("Arial", 14, "bold"))
    titulo_principal.grid(row=0, column=0, pady=(0, 15))

    # Container para as telas
    global container_telas
    container_telas = tk.Frame(frame_principal)
    container_telas.grid(row=1, column=0, sticky="nsew")
    container_telas.columnconfigure(0, weight=1)
    container_telas.rowconfigure(0, weight=1)

    # Criar todas as telas
    criar_tela_painel_botoes()
    criar_tela_painel_adicao_automacao()
    criar_tela_painel_texto_area_transferencia()

    # =====================================================#
    ## Funções para sistema de rótulos ##
    # =====================================================#

    def abrir_selecao_rotulos():
        """Abre um menu com os rótulos criados para filtrar os botões"""
        global rotulo_filtro_atual, lista_rotulos_criados

        menu = tk.Menu(janela, tearoff=0, font=("Arial", 9))

        # ✅ Opção "Mostrar Tudo" sempre no topo
        menu.add_command(
            label="📋 Mostrar Tudo",
            command=lambda: filtrar_por_rotulo(None)
        )
        menu.add_separator()

        # Adiciona rótulos únicos
        rotulos_unicos = sorted(set(lista_rotulos_criados))
        if rotulos_unicos:
            for rotulo in rotulos_unicos:
                menu.add_command(label=f"🏷️ {rotulo}", command=lambda r=rotulo: filtrar_por_rotulo(r))
        else:
            menu.add_command(label="(Nenhum rótulo criado)", state="disabled")

        menu.tk_popup(janela.winfo_rootx() + 20, janela.winfo_rooty() + 100)
        menu.bind("<FocusOut>", lambda e: menu.destroy())

    def filtrar_por_rotulo(rotulo_selecionado):
        """Filtra os botões exibidos pelo rótulo selecionado"""
        global rotulo_filtro_atual
        rotulo_filtro_atual = rotulo_selecionado
        atualizar_painel_botoes()

        # Feedback visual opcional
        if rotulo_selecionado:
            titulo_principal.config(text=f"{rotulo_selecionado}")
        else:
            titulo_principal.config(text="Painel de botões")

    # =====================================================#
    ## RODAPÉ COM BOTÕES DE GERENCIAMENTO (2 colunas) ##
    # =====================================================#

    # Frame para organizar os botões do rodapé em grid 2x2
    frame_rodape = tk.Frame(frame_principal)
    frame_rodape.grid(row=2, column=0, pady=10)
    frame_rodape.columnconfigure(0, weight=1)
    frame_rodape.columnconfigure(1, weight=1)

    # Coluna 0: Botão SALVAR
    btn_salvar_lista = tk.Button(
        frame_rodape,
        text="Salvar",
        command=salvar_lista_de_automacoes,
        width=18,
        height=2,
        bg="#9C27B0",
        fg="white",
        font=("Arial", 7),
        relief=tk.RAISED,
        cursor="hand2",
        wraplength=160,
        justify="center",
        anchor="center",
        padx=8, pady=4
    )
    btn_salvar_lista.grid(row=0, column=0, padx=5, pady=2, sticky="ew")

    # Coluna 1: Botão IMPORTAR
    btn_importar_lista = tk.Button(
        frame_rodape,
        text="Importar",
        command=importar_lista_de_automacao,
        width=18,
        height=2,
        bg="#673AB7",
        fg="white",
        font=("Arial", 7),
        relief=tk.RAISED,
        cursor="hand2",
        wraplength=160,
        justify="center",
        anchor="center",
        padx=8, pady=4
    )
    btn_importar_lista.grid(row=0, column=1, padx=5, pady=2, sticky="ew")

    # Linha 1: Botão SELECIONAR RÓTULOS (ocupa as 2 colunas)
    btn_selecionar_rotulos = tk.Button(
        frame_rodape,
        text="🏷️Rótulos",
        command=abrir_selecao_rotulos,  # ✅ Nova função
        width=20,
        height=2,
        bg="#3F51B5",  # Azul diferente
        fg="white",
        font=("Arial", 10, "bold")
    )
    btn_selecionar_rotulos.grid(row=1, column=0, columnspan=2, pady=8, sticky="ew")

    # Mensagem de instrução (abaixo do rodapé)
    instrucao = tk.Label(
        frame_principal,
        text="Ter tempo é possuir o bem mais precioso para quem aspira a grandes coisas.",
        font=("Arial", 7, "italic"),
        fg="#666"
    )
    instrucao.grid(row=3, column=0, pady=(0, 10))

    # Mostrar tela inicial
    mostrar_tela("painel_botoes")

    janela.mainloop()


def criar_tela_painel_botoes():
    """Cria o painel principal de botões"""
    global frame_painel_botoes, canvas, frame_botoes, scrollbar

    frame_painel_botoes = tk.Frame(container_telas)
    frame_painel_botoes.grid(row=0, column=0, sticky="nsew")
    frame_painel_botoes.columnconfigure(0, weight=1)
    frame_painel_botoes.rowconfigure(0, weight=1)

    # Canvas com scroll
    canvas = tk.Canvas(frame_painel_botoes, height=620)
    scrollbar = tk.Scrollbar(frame_painel_botoes, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    frame_botoes = tk.Frame(canvas)
    canvas_window = canvas.create_window((0, 0), window=frame_botoes, anchor="nw")

    # Configurar colunas do frame_botoes
    frame_botoes.columnconfigure(0, weight=1)  # Espaçador esquerdo
    frame_botoes.columnconfigure(1, weight=0)  # Coluna botões esquerda
    frame_botoes.columnconfigure(2, weight=0)  # Coluna botões direita
    frame_botoes.columnconfigure(3, weight=1)  # Espaçador direito

    # Scroll unificado
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

    # POSICIONAMENTO
    scrollbar.grid(row=0, column=0, sticky="ns")
    canvas.grid(row=0, column=1, sticky="nsew")

    # Atualizar botões inicialmente
    atualizar_painel_botoes()


def criar_tela_painel_adicao_automacao():
    """Cria o painel de adição de automação"""
    global frame_painel_adicao_automacao

    frame_painel_adicao_automacao = tk.Frame(container_telas)
    frame_painel_adicao_automacao.grid(row=0, column=0, sticky="nsew")

    # Título
    titulo = tk.Label(
        frame_painel_adicao_automacao,
        text="Painel de Adição de Automação",
        font=("Arial", 14, "bold"),
        pady=20
    )
    titulo.pack()

    # Botão texto para área de transferência
    btn_texto_transferencia = tk.Button(
        frame_painel_adicao_automacao,
        text="Texto para a Área de Transferência",
        command=abrir_painel_texto_area_transferencia,
        width=35,
        height=3,
        bg="#2196F3",
        fg="white",
        font=("Arial", 10),
        relief=tk.RAISED,
        cursor="hand2"
    )
    btn_texto_transferencia.pack(pady=20)

    # Botão voltar
    btn_voltar = tk.Button(
        frame_painel_adicao_automacao,
        text="Voltar",
        command=voltar_para_painel_de_botoes,
        width=20,
        height=2,
        bg="#9E9E9E",
        fg="white",
        font=("Arial", 10),
        relief=tk.RAISED,
        cursor="hand2"
    )
    btn_voltar.pack(pady=20)


def criar_tela_painel_texto_area_transferencia():
    """Cria o painel de adição de texto para área de transferência"""
    global frame_painel_texto_area_transferencia, entry_nome_botao, entry_texto_conteudo, btn_salvar_ref, combobox_rotulos_ref

    frame_painel_texto_area_transferencia = tk.Frame(container_telas)
    frame_painel_texto_area_transferencia.grid(row=0, column=0, sticky="nsew")

    # Título
    titulo = tk.Label(
        frame_painel_texto_area_transferencia,
        text="Adicionar Texto para Área de Transferência",
        font=("Arial", 12, "bold"),
        pady=10,
        wraplength=400
    )
    titulo.pack()

    # Label e campo para nome do botão
    label_nome = tk.Label(
        frame_painel_texto_area_transferencia,
        text="Nome do Botão:",
        font=("Arial", 10),
        anchor="w"
    )
    label_nome.pack(fill=tk.X, padx=10, pady=(10, 5))

    entry_nome_botao = tk.Entry(
        frame_painel_texto_area_transferencia,
        font=("Arial", 10),
        width=40
    )
    entry_nome_botao.pack(fill=tk.X, padx=10, pady=5)

    # ✅ NOVO: Campo de rótulos com Combobox
    label_rotulos = tk.Label(
        frame_painel_texto_area_transferencia,
        text="Rótulos (separe por vírgula):",
        font=("Arial", 10),
        anchor="w"
    )
    label_rotulos.pack(fill=tk.X, padx=10, pady=(10, 5))

    combobox_rotulos_ref = tk.Entry(
        frame_painel_texto_area_transferencia,
        font=("Arial", 10),
        width=40
    )
    combobox_rotulos_ref.pack(fill=tk.X, padx=10, pady=5)

    # Dica abaixo do campo
    dica_rotulos = tk.Label(
        frame_painel_texto_area_transferencia,
        text="Ex: trabalho, pessoal, urgente | Digite ou selecione um existente",
        font=("Arial", 8),
        fg="#666",
        anchor="w"
    )
    dica_rotulos.pack(fill=tk.X, padx=10, pady=(0, 5))

    # Label e campo para texto
    label_texto = tk.Label(
        frame_painel_texto_area_transferencia,
        text="Texto para Copiar:",
        font=("Arial", 10),
        anchor="w"
    )
    label_texto.pack(fill=tk.X, padx=10, pady=(10, 5))

    entry_texto_conteudo = tk.Text(
        frame_painel_texto_area_transferencia,
        font=("Arial", 10),
        width=40,
        height=8,
        wrap=tk.WORD
    )
    entry_texto_conteudo.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    # Frame para botões
    frame_botoes_acoes = tk.Frame(frame_painel_texto_area_transferencia)
    frame_botoes_acoes.pack(fill=tk.X, padx=10, pady=20)

    # Botão salvar
    btn_salvar_ref = tk.Button(
        frame_botoes_acoes,
        text="Salvar",
        command=salvar_texto_para_area_de_transferencia,
        width=15,
        height=2,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 10, "bold"),
        relief=tk.RAISED,
        cursor="hand2"
    )
    btn_salvar_ref.pack(side=tk.LEFT, padx=10)

    # Botão voltar
    btn_voltar = tk.Button(
        frame_botoes_acoes,
        text="Voltar",
        command=lambda: [resetar_edicao_se_necessario(), abrir_painel_adicao_automacao()],
        width=15,
        height=2,
        bg="#9E9E9E",
        fg="white",
        font=("Arial", 10),
        relief=tk.RAISED,
        cursor="hand2"
    )
    btn_voltar.pack(side=tk.RIGHT, padx=10)


def mostrar_tela(nome_tela):
    """Mostra a tela especificada e esconde as outras"""
    global titulo_principal  # ✅ Acessa o título

    telas = {
        "painel_botoes": frame_painel_botoes,
        "painel_adicao_automacao": frame_painel_adicao_automacao,
        "painel_texto_area_transferencia": frame_painel_texto_area_transferencia
    }

    # ✅ Mostra/esconde o título apenas no painel principal
    if nome_tela == "painel_botoes":
        titulo_principal.grid()  # Mostra
    else:
        titulo_principal.grid_remove()  # Esconde (mantém configuração para restaurar depois)

    # Gerencia as telas normais
    for nome, frame in telas.items():
        if nome == nome_tela:
            frame.tkraise()
        else:
            frame.lower()


def atualizar_painel_botoes():
    """Atualiza o grid de botões no painel principal (com filtro de rótulos)"""
    global rotulo_filtro_atual

    # Limpa botões existentes
    for widget in frame_botoes.winfo_children():
        widget.destroy()

    frame_botoes.columnconfigure(0, weight=1)
    frame_botoes.columnconfigure(1, weight=0)
    frame_botoes.columnconfigure(2, weight=0)
    frame_botoes.columnconfigure(3, weight=1)

    from indice import botoes as botoes_atualizados, ROTULOS_POR_BOTAO

    # ✅ Filtra botões por rótulo se necessário
    botoes_para_exibir = []
    for nome, callback in botoes_atualizados:
        chave = getattr(callback, 'chave', None)
        if rotulo_filtro_atual and chave:
            rotulos_do_botao = ROTULOS_POR_BOTAO.get(chave, [])
            if rotulo_filtro_atual not in rotulos_do_botao:
                continue  # Pula botão que não tem o rótulo filtrado
        botoes_para_exibir.append((nome, callback, chave))

    # Adiciona botões filtrados
    for i, (texto, comando, chave) in enumerate(botoes_para_exibir):
        linha = i // 2
        coluna_grid = 1 if (i % 2 == 0) else 2

        btn = tk.Button(
            frame_botoes,
            text=texto,
            command=comando,
            width=18,
            height=2,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 9),
            relief=tk.RAISED,
            cursor="hand2",
            wraplength=160,
            justify="center",
            anchor="center",
            padx=8, pady=4
        )
        btn.grid(row=linha, column=coluna_grid, padx=5, pady=5, sticky="ew")

        if chave:
            btn.bind("<Button-3>", lambda e, ch=chave, nm=texto: mostrar_menu_contextual(e, ch, nm))

    # Posiciona o botão "+"
    indice_botao_mais = len(botoes_para_exibir)
    linha_mais = indice_botao_mais // 2
    coluna_mais = 1 if (indice_botao_mais % 2 == 0) else 2

    btn_adicionar = tk.Button(
        frame_botoes,
        text="+",
        command=abrir_painel_adicao_automacao,
        width=18,
        height=2,
        bg="#FF9800",
        fg="white",
        font=("Arial", 9, "bold"),
        relief=tk.RAISED,
        cursor="hand2",
        wraplength=160,
        justify="center",
        anchor="center",
        padx=8, pady=4
    )
    btn_adicionar.grid(row=linha_mais, column=coluna_mais, padx=5, pady=5, sticky="ew")

    frame_botoes.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))


if __name__ == "__main__":
    criar_interface()


# =====================================================#
## Funções de salvar e importar lista de automações ##
# =====================================================#

def salvar_lista_de_automacoes():
    """Salva a lista de automações em um arquivo JSON"""
    arquivo = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        title="Salvar lista de automações",
        initialfile="automacoes_repyta.json"
    )

    if arquivo:
        try:
            dados = indice.get_estado_automacoes()
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("✅ Sucesso", f"Lista salva em:\n{arquivo}")
        except Exception as e:
            messagebox.showerror("❌ Erro", f"Erro ao salvar arquivo:\n{e}")


def importar_lista_de_automacao():
    """Importa a lista de automações de um arquivo JSON"""
    arquivo = filedialog.askopenfilename(
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        title="Importar lista de automações"
    )

    if arquivo:
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)

            # Confirmação antes de sobrescrever
            from indice import botoes as botoes_indice, TEXTOS_PARA_COLAR as textos_indice
            if botoes_indice or textos_indice:
                resposta = messagebox.askyesno(
                    "⚠️ Confirmar",
                    "Isso substituirá sua lista atual de automações.\nDeseja continuar?"
                )
                if not resposta:
                    return

            # Restaura o estado
            set_estado_automacoes(dados)

            # ✅ RECONSTRÓI lista_rotulos_criados a partir dos rótulos importados
            global lista_rotulos_criados
            lista_rotulos_criados = []
            from indice import ROTULOS_POR_BOTAO
            for rotulos in ROTULOS_POR_BOTAO.values():
                for rotulo in rotulos:
                    if rotulo not in lista_rotulos_criados:
                        lista_rotulos_criados.append(rotulo)

            # ✅ GARANTE QUE ESTÁ NA TELA DE BOTÕES E ATUALIZA
            mostrar_tela("painel_botoes")
            atualizar_painel_botoes()

            # ✅ FORÇA ATUALIZAÇÃO DA INTERFACE
            janela.update_idletasks()
            janela.update()

            messagebox.showinfo("✅ Sucesso", "Lista importada com sucesso!")

        except json.JSONDecodeError:
            messagebox.showerror("❌ Erro", "Arquivo inválido ou corrompido.")
        except Exception as e:
            messagebox.showerror("❌ Erro", f"Erro ao importar arquivo:\n{e}")

def reconstruir_lista_rotulos():
    """
    Reconstrói lista_rotulos_criados a partir de ROTULOS_POR_BOTAO
    Garantir que lista_rotulos_criados nunca fique dessincronizada, você pode criar uma função utilitária:
    E chamá-la sempre que necessário (após importar, ou até ao iniciar a interface, se quiser carregar rótulos salvos previamente).
    """
    global lista_rotulos_criados
    from indice import ROTULOS_POR_BOTAO
    lista_rotulos_criados = []
    for rotulos in ROTULOS_POR_BOTAO.values():
        for rotulo in rotulos:
            if rotulo not in lista_rotulos_criados:
                lista_rotulos_criados.append(rotulo)

