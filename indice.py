# indice.py
import pyautogui
import pyperclip

# Variáveis globais
botoes = [
    ("Exemplo 1", lambda: colar_texto('exemplo_1'))
]

TEXTOS_PARA_COLAR = {
    'exemplo_1': """Bem vindo ao Repyta"""
}

# ✅ NOVO: Dicionário para armazenar rótulos por chave de botão
ROTULOS_POR_BOTAO = {}

# Contador para próxima chave numérica
_proxima_chave_num = 1


def proxima_chave():
    """Retorna a próxima chave numérica disponível"""
    global _proxima_chave_num
    chave = str(_proxima_chave_num)
    _proxima_chave_num += 1
    return chave


def colar_texto(chave_do_texto):
    print(f"\nFunção 'colar_texto' chamada com a chave: {chave_do_texto}")
    pyautogui.FAILSAFE = True

    texto_final = TEXTOS_PARA_COLAR.get(chave_do_texto)

    if not texto_final:
        print(f"Erro: Chave '{chave_do_texto}' não encontrada no dicionário de textos.")
        return

    try:
        pyperclip.copy(texto_final)
        pyautogui.hotkey('ctrl', 'v')
        print(f"Texto '{chave_do_texto}' colado com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro no PyAutoGUI: {e}")


# =====================================================#
## Funções de gerenciamento de estado para salvar/importar ##
# =====================================================#

def criar_callback_com_chave(chave_texto):
    """Cria um callback com a chave armazenada como atributo"""

    def callback():
        colar_texto(chave_texto)

    callback.chave = chave_texto  # Permite recuperar a chave ao salvar
    return callback


def get_estado_automacoes():
    """Retorna o estado atual das automações para salvamento"""
    botoes_salvar = []

    for nome, callback in botoes:
        chave = getattr(callback, 'chave', None)
        if chave is None:
            for key, texto in TEXTOS_PARA_COLAR.items():
                if hasattr(callback, '__closure__') and callback.__closure__:
                    try:
                        if len(callback.__closure__) > 0:
                            chave_closure = callback.__closure__[0].cell_contents
                            if chave_closure == key:
                                chave = key
                                break
                    except:
                        pass
        if chave is not None:
            botoes_salvar.append((nome, chave))

    return {
        'textos': TEXTOS_PARA_COLAR.copy(),
        'botoes': botoes_salvar,
        'rotulos': ROTULOS_POR_BOTAO.copy(),  # ✅ Salva rótulos
        'proxima_chave': _proxima_chave_num
    }


def set_estado_automacoes(dados):
    """Restaura o estado das automações a partir de dados carregados"""
    global TEXTOS_PARA_COLAR, botoes, _proxima_chave_num, ROTULOS_POR_BOTAO

    TEXTOS_PARA_COLAR.clear()
    TEXTOS_PARA_COLAR.update(dados.get('textos', {}))

    # ✅ Restaura rótulos
    ROTULOS_POR_BOTAO.clear()
    ROTULOS_POR_BOTAO.update(dados.get('rotulos', {}))

    _proxima_chave_num = dados.get('proxima_chave', 1)

    botoes.clear()
    for nome_botao, chave in dados.get('botoes', []):
        botoes.append((nome_botao, criar_callback_com_chave(chave)))