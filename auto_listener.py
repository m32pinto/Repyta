# =====================================================#
## Início Bibliotecas ##
# =====================================================#

import pyautogui
from pynput import keyboard
from auto_teste import colar_texto # 1. Importamos nossa nova função
from auto_teste import colar_texto_sequencia
from dicts import MAPEAMENTO_ATALHOS

# =====================================================#
## Fim Bibliotecas ##
# =====================================================#

# =====================================================#9
## Início Função callback par lidar com multiplas chaves (criar_callback_sequencia) ##
# =====================================================#

def criar_callback_sequencia(chaves_str):
    pyautogui.FAILSAFE = True
    """
    Cria um callback que chama colar_textos_sequencia com as chaves fornecidas.
    """
    chaves = chaves_str.split(',') # Divide a ‘string’ por vírgula
    return lambda: colar_texto_sequencia(chaves)

# =====================================================#
## Fim   Função callback par lidar com multiplas chaves (criar_callback_sequencia) ##
# =====================================================#

# =====================================================#
## Início Função criar_callbacks ##
# =====================================================#

# --- 3. Função "Fábrica" de Callbacks ---
# Isso é necessário para garantir que o atalho certo
# chame a chave certa (evita um bug comum de 'closures' em loops)
def criar_callback(chave_do_texto):
    pyautogui.FAILSAFE = True
    # 'lambda' cria uma pequena função que chama 'colar_texto'
    # com a chave que passamos.
    return lambda: colar_texto(chave_do_texto)

# =====================================================#
## Fim Função criar_callbacks ##
# =====================================================#

# =====================================================#
## Início hotkeys_para_ouvir ##
# =====================================================#

# --- 4. Montagem do Dicionário para o Pynput ---
# O GlobalHotKeys espera um dicionário no formato:
# { 'atalho_string': funcao_callback }
hotkeys_para_ouvir = {}
pyautogui.FAILSAFE = True
for atalho, chave in MAPEAMENTO_ATALHOS.items():
    if '.' in chave: # Se a chave contém vírgula, é uma sequência
        hotkeys_para_ouvir[atalho] = criar_callback_sequencia(chave)
    else:
        hotkeys_para_ouvir[atalho] = criar_callback(chave)

# --- 5. Configuração e Início do Listener ---
print("Ouvinte de múltiplos atalhos iniciado.")
print("Atalhos configurados:")
for atalho, chave in MAPEAMENTO_ATALHOS.items():
    print(f"  {atalho}  ->  Texto: '{chave}'")
print("!!! ESTE TERMINAL DEVE PERMANECER ABERTO !!!")

with keyboard.GlobalHotKeys(hotkeys_para_ouvir) as listener:
    listener.join()

# =====================================================#
## Fim hotkeys_para_ouvir ##
# =====================================================#



# =====================================================#
## Conceitos ##

#Função callbacks
##Ao usar callbacks, é possível definir comportamentos específicos para diferentes eventos.
##Por exemplo, aciona-se um callback quando o usuário clica em um botão,
##insere dados em um campo de entrada ou seleciona uma opção em um menu suspenso.

# =====================================================#