# =====================================================#
## Início Bibliotecas ##
# =====================================================#

import pyautogui
import pyperclip
from dicts import TEXTOS_PARA_COLAR

# =====================================================#
## Fim Bibliotecas ##
# =====================================================#

# =====================================================#
## Início função colar texto ##
# =====================================================#

# 2. A função agora recebe um argumento: a 'chave_do_texto'
def colar_texto(chave_do_texto):
    print(f"\nFunção 'colar_texto' chamada com a chave: {chave_do_texto}")
    pyautogui.FAILSAFE = True

    # 3. Busca o texto no dicionário
    texto_final = TEXTOS_PARA_COLAR.get(chave_do_texto)

    # 4. Se não encontrar o texto, avisa e para
    if not texto_final:
        print(f"Erro: Chave '{chave_do_texto}' não encontrada no dicionário de textos.")
        return

    try:
        # 5. Clica no centro (ajuste 960, 540 se precisar)
        pyautogui.doubleClick(x=471, y=914)
        pyautogui.sleep(0.1)

        # 6. Copia e Cola
        pyperclip.copy(texto_final)
        ## pyautogui.sleep(2) tentativa de ajeitar o erro do fim da função colar texto sequência.
        pyautogui.hotkey('ctrl', 'v')
        
        print(f"Texto '{chave_do_texto}' colado com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro no PyAutoGUI: {e}")

# Teste (se você rodar 'python3 teste.py' diretamente)
if __name__ == "__main__":
    import time
    print("Iniciando teste da função em 3 segundos...")
    print("Clique onde o texto deve aparecer!")
    time.sleep(3)
    
    print("\nTestando chave 'solicitacao_de_registro_profissional'...")
    colar_texto('solicitacao_de_registro_profissional')
    time.sleep(2)
    
    print("\nTestando chave 'saudacao'...")
    colar_texto('saudacao')

# =====================================================#
## Fim função colar_texto ##
# =====================================================#

# =====================================================#
## Início função colar_texto_sequência##
# =====================================================#

def colar_texto_sequencia(chaves):

    """
    Cola sequencialmente os textos associados às chaves fornecidas.
    Espera 2 segundos entre cada colagem.
    Após a última colagem, pressiona Enter.
    """
    print(f"\nFunção 'colar_textos_sequencia' chamada com chaves: {chaves}")
    pyautogui.FAILSAFE = True

    # Verifica se a lista de chaves está vazia

    if not chaves:
        print("Erro: lista chaves vazia")
        return

    # Cria uma lista de chaves para iterar

    for chave in chaves:
        print(f"Colando texto: {chave}")
        pyautogui.press('backspace')
        colar_texto(chave) # chama a função existente
        pyautogui.sleep(2) # espera 2 segundos
        pyautogui.press('enter')
        pyautogui.sleep(2)

    print("\nTextos colados com sucesso")

    # Chamada de função enviar_imagens()
    enviar_imagens()

    # Construção de lógica para inicio de funções de automatizações
    """
    if chave is 'texto_1.1,texto_1.2,texto_1.3,texto_1.4,texto_1.5':
        enviar_imagens() # < - - Chamada de função
    else:
        verificacao_de_registro_nao_deferidos()
    """


# =====================================================#
## fim função colar texto sequência ##
# =====================================================#

# =====================================================#
## Início função enviar imagens de benefícios e sobre técnico que faz##
# =====================================================#

#Envia 3 imagens seguindo a sequência de ações definidas

def enviar_imagens():
    print("\n Iniciando o envio de imagens (Benefícios e sobre técnico que faz)")
    pyautogui.FAILSAFE = True

    try:
        # 1 - Clicar no anexar arquivos
        pyautogui.click(x=411, y=978) # Posição do botão anexar arquivos
        pyautogui.sleep(2)

        # 2 - Clica em documentos
        pyautogui.click(x=93, y=264) # Documentos 
        pyautogui.sleep(2)

        # 3 - Clicar na pasta trabalho
        pyautogui.doubleClick(x=249, y=331) # Documentos 
        pyautogui.sleep(2)

        # 4 - Clicar na pasta folders_tecnico_que_faz
        pyautogui.doubleClick(x=231, y=177)
        pyautogui.sleep(2)
         # Enter após digitar

        # 5 - Selecionar todos os arquivos
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.sleep(2)

        # 6 = Clicar em abrir
        pyautogui.click(x=492, y=474)  
        pyautogui.sleep(2)

        # 7 = Clicar em enviar
        pyautogui.click(x=627, y=732)  
        

        print("Envio de imagens concluído com sucesso.")

    except Exception as e:
       print(f"Ocorreu um erro ao enviar as imagens: {e}")

# Construção da função de verificação de profissionais ainda não deferidos

"""
def verificacao_de_registro_nao_deferidos():
    print("\nIniciando cliques para registro ainda não deferidos")
    pyautogui.FAILSAFE = True

    try:

        # 1 - clique na barra de texto e recarregue a página  
        pyautogui.click(x=1236, y=380)
        pyautogui.hotkey('ctrl','r')
        pyautogui.sleep(2)

        # 2 - clique na barra de texto e colar informação 
        pyautogui.click(x=1236, y=380)
        pyautogui.sleep(2)
        pyautogui.hotkey('ctrl','v')
        pyautogui.sleep(2)


        # 3 - Clicar em ver itens
        pyautogui.click(x=1834, y=490)
        pyautogui.sleep(2)

        ##pyautogui.scroll(5)
        ##pyautogui.sleep(2)



    except Exception as e:
        print(f"Ocorreu um erro na automatização: {e}")
"""