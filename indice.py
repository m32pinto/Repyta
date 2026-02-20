#indice.py

import pyautogui
import pyperclip

TEXTOS_PARA_COLAR = {

    'chave_1': """conteúdo""",

}

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
