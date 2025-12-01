# =====================================================#
## Início Bibliotecas ##
# =====================================================#

import pyautogui
import pyperclip

# =====================================================#
## Fim Bibliotecas ##
# =====================================================#

# =====================================================#
## Início da Variável de dicionário ##
# =====================================================#
TEXTOS_PARA_COLAR = {
    
    'solicitacao_de_registro_profissional': """SOLICITAÇÃO DE REGISTRO PROFISSIONAL

    Entre no site: https://corporativo.sinceti.net.br/app/view/sight/externo.php?form=CadastrarProfissional e preencha o formulário, sendo obrigatório o preenchimento nos espaços que conterem um asterisco vermelho. Segue abaixo os documentos necessários para solicitação de Registro Profissional:

    1. Diploma ou certificado do ensino técnico;

    2. Histórico do ensino técnico com indicação das cargas horárias cursadas;

    3. RG (frente e verso)

    4. CPF (frente e verso)

    5. Comprovantes de endereço atualizado ou declaração de residência;

    6. Foto 3x4, de preferência de fundo branco;

    7. Título de eleitor (frente e verso)

    8. Prova de quitação com a Justiça Eleitoral (Certidão de quitação eleitoral)

    9. Prova de quitação com o Serviço Militar (sexo masculino).

    Obs.: anexar os documentos digitalizados em PDF ou JPG individualmente.
    Colocar um e-mail e no final gerar o boleto de análise de registo.

    Após 24h do pagamento, ao constar no sistema, a sua solicitação é enviada para ser analisada.""",
    
    'solicitacao_de_interrupcao_de_registro': """SOLICITAÇÃO DE INTERRUPÇÃO DE REGISTRO.
    
    Para solicitar a INTERRUPÇÃO DE REGISTRO proceda da seguinte forma:

    Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/

    Selecione a opção PROTOCOLOS, em seguida CADASTRAR;

    Em GRUPO DE ASSUNTO escolha a opção PROFISSIONAL;

    Em ASSUNTO, vá até a opção SOLICITAÇÃO DE INTERRUPÇÃO DE REGISTRO PROFISSIONAL;

    Em DESCRIÇÃO DO PROTOCOLO, descreva os motivos pelos quais deseja solicitar a interrupção do registro;

    Em DOCUMENTOS ANEXOS, clique em NOVO ARQUIVO, em seguida anexe um documento comprobatório que informe que você não possui atividade laborativa compatível com a área técnica (declaração de não ocupação de cargo ou atividade na área de sua formação técnica profissional, constando nome completo e CPF, assinada pelo requerente e datada).

    Por fim, clique em CADASTRAR.""",
    
    'solicitacao_de_reativacao_profissional_inativos': """SOLICITAÇÃO DE REATIVAÇÃO PROFISSIONAL (INATIVOS)

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/

    2. Selecione a opção PROTOCOLOS, em seguida CADASTRAR;

    3. Em GRUPO DE ASSUNTO escolha a opção PROFISSIONAL;

    4. Em ASSUNTO, vá até a opção REATIVAÇÃO DE REGISTRO - PROFISSIONAL INATIVO ;

    5. Em DESCRIÇÃO DO PROTOCOLO, descreva os motivos pelos quais deseja solicitar a reativação de registro.

    6. selecione a opção  “Declaro, sob as penas da Lei, serem verdadeiras as informações aqui declaradas”

    7. Se precisar anexar mais de um documento, clique em "NOVO ARQUIVO" que encontra-se localizado acima do campo "responder de responder despacho".

    Aconselhamos para fins de atualização de dados cadastrais, encaminhar os seguintes documentos no protocolo:

    1. RG;
    2. CPF;
    3. Comprovantes de endereço atualizado ou declaração de residência;
    4. Foto 3x4, de preferência de fundo branco;
    5. Título de eleitor;
    6. Prova de quitação com a Justiça Eleitoral (comprovante de votação ou certidão de quitação eleitoral).""",
    
    'procotolo_de_outros': """PROTOCOLO DE OUTROS

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR;

    3. GRUPO DE ASSUNTO: profissional;

    4. ASSUNTO: opção de outros;

    5. DESCRIÇÃO DO PROTOCOLO: “descreva o motivo do protocolo”.

    6. Clique em "NOVO ARQUIVO" que encontra-se localizado acima do campo "CADASTRAR".

    7. Anexe uma documentação comprobatória.""",

    'protocolo_de_reativacao_de_registro': """PROTOCOLO DE REATIVAÇÃO DE REGISTRO.

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR;

    3. GRUPO DE ASSUNTO: profissional;

    4. ASSUNTO: Reativação de Registro–Profissional;

    5. Em DESCRIÇÃO DO PROTOCOLO, descreva os motivos pelos quais deseja solicitar a reativação de registro;

    6. Selecione a opção “Declaro, sobre as penas da Lei, serem verdadeiras as informações aqui declaradas”

    7. CADASTRAR.

    OBS.: Realize o pagamento do seu boleto referente a taxa de análise de Registro no valor de R$63,83 (Lembrando que o prazo para compensação de boleto é de 24 a 72 horas).""",

    'protocolo_de_reativacao_definitivo_ou_renovacao_de_provisorio': """PROTOCOLO DE REGISTRO DEFINITIVO OU RENOVAÇÃO DE PROVISÓRIO.

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR;

    3. GRUPO DE ASSUNTO: profissional;

    4. ASSUNTO: Solicitação de Registro Definitivo caso *haja diploma e histórico* ou renovação de registro provisório caso *haja declaração de conclusão de curso e histórico*

    5. Em DESCRIÇÃO DO PROTOCOLO, descreva os motivos pelos quais deseja solicitar o Registro Definitivo ou Renovação do Provisório.

    6. Selecione a opção  “Declaro, sobre as penas da Lei, serem verdadeiras as informações aqui declaradas”

    7. Clique em "NOVO ARQUIVO" que encontra-se localizado acima do campo "CADASTRAR".

    8. Anexe a documentação solicitada.

    9. Cadastrar.""",

    'emissao_de_certidao_de_quitacao_de_pf': """EMISSÃO DE CERTIDÃO DE QUITAÇÃO DE PESSOA FÍSICA:

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/

    2. Selecione a opção CERTIDÕES em seguida SOLICITAR CERTIDÃO;

    3. Tipo de Certidão: Certidão de quitação de pessoa física;

    4. Confirme as suas informações;

    5. Preencha o código de segurança;

    6. Cadastrar...

    7. Selecione novamente a opção (Certidão de quitação de pessoa física) e ficará disponível a opção IMPRIMIR.""",

    'emissao_de_carteira_digital': """EMISSÃO DE CARTEIRA DIGITAL:

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/

    2. Selecione a opção IMPRESSÃO DE CARTEIRA.""",

    'solicitacao_de_carteira_fisica': """SOLICITAÇÃO DE CARTEIRA FÍSICA:
    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR;

    3. GRUPO DE ASSUNTO: profissional;

    4. ASSUNTO: opção de solicitação de carteira profissional;

    5. DESCRIÇÃO DO PROTOCOLO: “Solicito a emissão da carteira profissional junto ao crt02”.""",

    'inclusao_de_foto': """INCLUSÃO DE FOTO

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR;

    3. GRUPO DE ASSUNTO: profissional;

    4. ASSUNTO: selecione a opção de inclusão de foto;

    5. DESCRIÇÃO DO PROTOCOLO: “Solicito a inclusão de foto para emissão de carteira”;

    6. Anexe dois documentos (FOTO 3X4 e RG ou CNH).""",

    'manual_instrutivo_para_geracao_de_anuidade': """*Manual Instrutivo para Geração de Anuidade*
    Este manual tem como objetivo orientar o usuário sobre como acessar e utilizar o sistema para gerar anuidades.

    *Passo 1: Acesso ao Sistema*

    1. Acesse o sistema utilizando seu CPF e senha pessoal, através do link: https://servicos.sinceti.net.br/ 

    *Passo 2: Navegação para a Geração de Anuidade*

    2. No canto superior da tela, localize e clique na aba ou menu denominado "Financeiro".

    *Passo 3: Seleção da Opção Anuidade*

    3. Dentro do menu Financeiro, encontre e selecione a opção específica para "Anuidade".

    *Passo 4: Escolha dos Anos em Aberto*

    4. Na página de Anuidade, selecione os anos referentes às anuidades em aberto.

    *Passo 5: Aceitação do Termo de Compromisso*

    5. Antes de prosseguir, é necessário concordar com o termo de compromisso relacionado à geração das anuidades.

    *Passo 6: Realização de Simulações e Seleção de Parcelas*

    6. Realize simulações conforme necessário e escolha o padrão de parcelas que melhor atenda às suas necessidades. ( informamos que caso haja juros e multa ou taxa em sua simulação, haverá acréscimos de acordo com a quantidade de parcelas escolhidas.)

    *Passo 7: Geração da Anuidade*

    7. Após escolher o padrão de parcelas desejado, clique na opção "Gerar Anuidade" para finalizar o processo.

    *Observações Finais:*

    - Certifique-se de revisar todas as informações inseridas antes de confirmar a geração da anuidade.
    - A data de vencimento dos boletos ficarão definidas para o último dia do mês de cada parcela.
    - Em caso de dúvidas ou problemas técnicos, entre em contato com o suporte técnico responsável.
    Este manual visa facilitar o processo de geração de anuidades no sistema, proporcionando uma experiência clara e eficiente para o usuário.   
    """,


    'protocolo_de_inclusao_de_especializacao_tecnica': """
    PROTOCOLO DE INCLUSÃO DE ESPECIALIZAÇÃO TÉCNICA

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR

    3. GRUPO DE ASSUNTO: profissional

    4. ASSUNTO: selecione a opção de “inclusão de especialização técnica”

    5. DESCRIÇÃO DO PROTOCOLO: “Solicito a inclusão de minha especialização técnica ao registro profissional”. 

    6. Selecione a opção “Declaro, sobre as penas da Lei, serem verdadeiras as informações aqui declaradas”

    7. Clique em "NOVO ARQUIVO" que encontra-se localizado acima do campo "CADASTRAR".""",


    'protocolo_inclusao_de_titulo': """PROTOCOLO INCLUSÃO DE TÍTULO:

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR

    3. GRUPO DE ASSUNTO: profissional

    4. ASSUNTO: selecione a opção de inclusão de Título

    5. DESCRIÇÃO DO PROTOCOLO: “Solicito a inclusão de título em meu registro profissional”

    6. Selecione a opção  “Declaro, sobre as penas da Lei, serem verdadeiras as informações aqui declaradas”

    7. clique em "NOVO ARQUIVO" que encontra-se localizado acima do campo "CADASTRAR".

    8. Anexe os documentos solicitados (Diploma e Histórico)

    OBS.: O profissional deve estar ADIMPLENTE para essa solicitação…""",


    'protocolo_de_alteracao_de_endereco': """PROTOCOLO DE ALTERAÇÃO DE ENDEREÇO:

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR

    3. GRUPO DE ASSUNTO: profissional

    4. ASSUNTO: selecione a opção de “Alteração de Endereço”

    5. DESCRIÇÃO DO PROTOCOLO: “Solicito a alteração do meu endereço”

    6. Anexe a documentação solicitada (COMPROVANTE DE RESIDÊNCIA).
    
    OBS.: O profissional deve estar ADIMPLENTE para essa solicitação.""",


    'saudacao': """Olá me chamo Marcos do setor de atendimento do CRT 02, como posso ajudar ?""",

    'verificacao': """Vou verificar, um momento.""",

    'documentacao_comprobatoria': """Por gentileza, envie um comprovante da sua urgência, pode ser PDF, conversa, email, edital... Fico no seu aguardo. 
    
    Essas informações são de forma oficial pela empresa ou plataforma de contratação se possível conter também a data limite para priorização.
    """,

    'aguardando_retorno': """Fico no aguardo do seu retorno.""",

    'algo_mais': """Ajudo em algo mais ?""",

    'texto_1.1': """Olá me chamo Marcos do setor de atendimento do CRT 02👨🏽‍💻""",
    'texto_1.2': """📣Antes de começar o atendimento gostaria de apresentar a nova ferramenta para os técnicos ganharem o mercados e serem vistos de forma privilegiadas *O técnico que faz* ✅ .""",
    'texto_1.3': """📣Segue o link para acessar a plataforma: https://tecnicoquefaz.crt02.gov.br/ e fazer seu cadastro. 🔗""",
    'texto_1.4': """📣Se preferir enviamos vídeos, guias para orientar o seu cadastro.🎥""",
    'texto_1.5': """📣O técnico que faz conecta profissionais registrados com a sociedade em geral: o técnico pode incluir seu currículo e oferecer serviços; a empresa pode encontrar candidatos habilitados para preencher suas vagas; e a sociedade pode encontrar opções de serviços com qualidade e responsabilidade técnica. Cadastre-se gratuitamente agora mesmo!🌐"""

    # Adicione quantos textos quiser
    # 'minha_chave_nova': "Meu novo texto rápido."
}

# =====================================================#
## Fim da Variável de dicionário ##
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
        pyautogui.doubleClick(2281, 1063)
        pyautogui.sleep(0.1)

        # 6. Copia e Cola
        pyperclip.copy(texto_final)
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

    print("\nTextos colados com sucesso")

    # Chamada de função enviar_imagens()
    enviar_imagens() # < - - Chamada de função


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
        pyautogui.click(x=371, y=1028) # Posição do botão anexar arquivos
        pyautogui.sleep(2)

        # 2 - Clicar em início
        pyautogui.click(x=65, y=471) # Posição do botão início
        pyautogui.sleep(2)

        # 3 - Clicar na lupa
        pyautogui.click(x=1757, y=382) # Posição na lupa
        pyautogui.sleep(2)

        # 4 - Escrever Documentos
        pyautogui.typewrite("documentos")
        pyautogui.sleep(2)
         # Enter após digitar

        # 5 - Apertar seta para baixo 2X + Enter
        pyautogui.press('down')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(2)

        # 6 = Clicar na lupa novamente
        pyautogui.click(x=1757, y=382)  # Posição na lupa
        pyautogui.sleep(2)

        # 7 - Escrever trabalho
        pyautogui.typewrite('Trabalho')
        pyautogui.sleep(2)
        pyautogui.press('down')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(2)

        # 8 - Clicar na lupa novamente
        pyautogui.click(x=1757, y=382)  # Posição na lupa
        pyautogui.sleep(2)

        # 9 - Escrever crt_02
        pyautogui.typewrite('crt_02')
        pyautogui.sleep(2)
        pyautogui.press('down')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(2)

        # 10 - Clicar na lupa novamente
        pyautogui.click(x=1757, y=382)  # Posição na lupa
        pyautogui.sleep(2)

        # 11 - Escrever folders_tecnico_que_faz
        pyautogui.typewrite('folders_tecnico_que_faz')
        pyautogui.sleep(2)
        pyautogui.press('down')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(2)

        # 12 - Apertar seta para cima 1X
        pyautogui.press('up')
        pyautogui.sleep(2)

        # 13 - Apertar seta para baixo 2X + Enter (ERRADO POIS TEM QUE SEGURAR O SHIFT)
        pyautogui.keyDown('shift+a')
        pyautogui.sleep(2)
        with pyautogui.hold('shift'):
            pyautogui.sleep(2)
            pyautogui.press(['down', 'down'])
            pyautogui.sleep(2)
        #pyautogui.press('down')
        #pyautogui.sleep(2)
        #pyautogui.press('enter')
        #pyautogui.sleep(2)

        # 14 - Apertar Enter
        pyautogui.press('enter')
        pyautogui.sleep(2)

        # 15 - CLiicar em enviar
        pyautogui.click(x=598, y=783)
        pyautogui.sleep(2)

        print("Envio de imagens concluído com sucesso.")

    except Exception as e:
       print(f"Ocorreu um erro ao enviar as imagens: {e}")


