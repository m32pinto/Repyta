✅ **Projeto: crt02_automatizacoes**  
Utilidades para o atendimento na autarquia.

---

🌟 **Introdução (Atualizações)**

1.0 - 30/11/2025

• Vamos iniciar mencionando as utilidades:

📌 **Apresentações**: Apresentação de técnico que faz.  
📝 **Textos rápidos personalizáveis**: Saudações, textos guias.  
🖼️ **Envio de imagens**: Envio de 3 folders (imagens)

As utilidades acima são acionadas por combinações de teclas, nesse primeiro momento sempre a primeira tecla contará com **shift** seguida de outra tecla do alfabeto.

---

💻 **Desenvolvimento (Explicação do código)**

  ### Teremos dois arquivos: 
 - `duas_telas_teste.py`  
 - `duas_telas_listener.py`

  #### `duas_telas_teste.py` é um dicionário e contém: 

  As bibliotecas: `pyautogui`, `pyperclip`

  📄 A variável **TEXTOS_PARA_COLAR**, a mesma contém **chaves** que são os títulos (strings) do texto que deseja-se enviar (solicitacao_de_registro_profissional, solicitacao_de_interrupcao_de_registro...), as chaves podem ter títulos sequênciais (texto_1.1, texto_1.2...) indicando uma conjunto de texto para serem enviados.

  🧩 Contém as **funções**:
  - `colar_texto` que recebe o argumento **chave_do_texto**: imprime qual a chave foi ativada, tenta clicar na barra de texto, espera 0.1s, copia o texto final (get do dicionário), se não encontrar, imprime “chave não encontrada”, depois clica e cola, espera 0.1s, imprime “colado com sucesso”. Em caso de erro, imprime “erro: e”.

  🧪 Tem um **teste** com `if` para colar uma chave somente se executado `duas_telas_teste.py`: conta 3s, no ponto onde clicar, se houver caixa de texto, colar conteúdo da chave **solicitacao_de_registro_profissional**, contar 2s, colar conteúdo da chave **saudacao**.

  🔄 A função `colar_texto_sequencia` recebe o argumento **chaves**: se não encontrar chaves, imprime mensagem. Itera lista de chaves com `for`, apaga caracteres indesejados com `backspace`, chama `colar_texto` para cada chave, espera 2s antes de pressionar `enter`, imprime “texto copiado completo”. No fim, chama `enviar_imagens()`.

  🖼️ A função `enviar_imagens` segue passo a passo:
  - Clique no botão de anexar arquivos no Blip.
  - Clique em “Início” no Gestor de Documentos.
  - Clique na lupa, digite “documentos”, selecione pasta com setas e Enter.
  - Clique na lupa, digite “trabalho”, selecione pasta com setas e Enter.
  - Clique na lupa, digite “crt_02”, selecione pasta com setas e Enter.
  - Clique na lupa, digite “folders_tecnico_que_faz”, selecione as 3 imagens.
  - Abre no pré-envio do Blip e aperta “enviar”.
  - Em caso de erro, imprime “erro: e”.

  #### `duas_telas_listener.py` é o “ouvido” que estará sempre mapeando o teclado, esperando um atalho a ser acionado e contém:

  As bibliotecas: `pynput` (usado `keyboard`), importamos duas funções de `duas_telas_teste`: `colar_texto` e `colar_texto_sequencia`.

  🎯 A função `criar_callback_sequencia` receberá **chaves_str** como argumento, dentro existe a variável **chaves** que receberá **chaves_str.split** e dividirá as strings por vírgula com `colar_texto_sequencia` recebendo **chaves**.

  ➕ Explicando melhor: recebemos os conteúdos nas **chaves** pela `colar_texto_sequencia` e as dividimos por vírgulas com `chaves_str.split(',')`.

  🗂️ A variável **MAPEAMENTO_DE_ATALHOS** armazenará os atalhos de teclado usados para iniciar uma automação — pode ser apenas colar do texto, sequência de texto, imagens, ou até sequência de textos + imagens.

  🔄 A função `criar_callbacks` será a garantia que o **atalho chame a chave correta**: receberá **chave_do_texto**, a lambda chamará `colar_texto` com a chave passada.

  🎮 A função `hot_keys_para_ouvir` — o `GlobalHotKeys` espera um dicionário no formato: `'atalho_string': funcao_callback`, para o atalho e chave no mapeamento de atalhos com os itens. Depois vem um teste: se tiver “.” (vírgula) na chave, é sequência → chamar `criar_callback_sequencia`, senão → chamar `criar_callback`.

  📢 Definimos mensagens para informar o funcionamento e acionamento de funções: logo para atalho e chave no mapeamento de atalhos, imprimimos o nome do **atalho** e a **chave**.

  🔄 Definimos uma função `loop` para ficar escutando as teclas do teclado (`keyboard`) como `listener` — o listener ficará o tempo todo mapeando o teclado.

---

📚 **Referências (Ferramentas utilizadas)**

📌 **PYAUTOGUI** - https://pyautogui.readthedocs.io/en/latest/  
📌 **PINPUT** - https://pypi.org/project/pynput/  
📌 **PYPERCLIP** - https://pypi.org/project/pyperclip/  
✨ **LMSTUDIO** - https://lmstudio.ai/  
✨ **QWEN** - https://lmstudio.ai/models/qwen/qwen3-vl-4b  
📌 **PYCHARM** - https://www.jetbrains.com/pt-br/pycharm/  
📌 **VSCODE** - https://code.visualstudio.com/
